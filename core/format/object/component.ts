import { MessageBuilder } from "../../builder/message";
import { Run, runcm } from "../command";
import { emoji } from "./emoji";

export type Button = {
    style: ButtonStyle;
    label?: string;
    emoji?: emoji;
    custom_id?: string;
    url?: string;
    disabled?: boolean;
    exec?: Run
}

export class ButtonBuilder {
    private style: ButtonStyle;
    private label?: string;
    private emoji?: emoji;
    private custom_id?: string;
    private url?: string;
    private disabled: boolean;
    private _exec?: Run
    constructor(op: Button) {
        this.style = op.style;
        this.disabled = op.disabled ?? false
        this.label = op.label;
        this.emoji = op.emoji;
        this.url = op.url;
        this.custom_id = op.custom_id;
        this._exec = op.exec;
    }

    public async exec(option: runcm) {
        if (this._exec === undefined) {
            return new MessageBuilder().setContent("No execute function for this Components").toJSON;
        } else {
            const result = await this._exec(option);
            return result.toJSON;
        }
    }

    get Style() {
        return this.style
    }

    get custom_ID() {
        return this.custom_id;
    }

    get toJSON() {
        if (this.style === ButtonStyle.Link && this.custom_id !== undefined) {
            throw new Error("Cannot use link style with custom id");
        }
        return {
            type: ComponentTypes.Button,
            label: this.label,
            style: this.style,
            custom_id: this.custom_id,
            emoji: this.emoji,
            url: this.url,
            disabled: this.disabled
        }
    }
}

export class ActionRowBuilder {
    buttons: ButtonBuilder[] = [];
    constructor() {

    }
    public addButton(button: ButtonBuilder) {
        this.buttons.push(button);
        return this;
    }
    public addButtons(button: ButtonBuilder[]) {
        button.forEach(button => this.buttons.push(button))
        return this;
    }
    get toJSON() {
        if (this.buttons.length !== 0) {
            return {
                type: ComponentTypes.ActionRow,
                components: this.buttons.map(e => e.toJSON)
            }
        }
        return {}

    }
}

export enum ButtonStyle {
    Primary = 1,
    Secondary = 2,
    Success = 3,
    Danger = 4,
    Link = 5,
}

export enum ComponentTypes {
    ActionRow = 1,
    Button = 2,
    StringSelect = 3,
    TextInput = 4,
    UserSelect = 5,
    RoleSelect = 6,
    MentionableSelect = 7,
    ChannelSelect = 8
}


export type components = {
    id?: string;
    components: components[] | Button[];
    type: ComponentTypes;
}