import { MessageBuilder } from "../builder/message";
import { interaction } from "./object/interactions";
import {message} from "./object/message";

export interface runcm {
    interaction: interaction;
}

export type Run = (options: runcm) => Promise<MessageBuilder>;

export type cmdSm = {
    name: string;
    description: string;
    option?: OptionBuilder[];
    exec?: Run;
}

export enum OptionType {
    SUB_COMMAND = 1,
    SUB_COMMAND_GROUP = 2,
    STRING = 3,
    INTEGER = 4,
    BOOLEAN = 5,
    USER = 6,
    CHANNEL = 7,
    ROLE = 8,
    MENTIONABLE = 9,
    NUMBER = 10,
    ATTACHMENT = 11,
}

type option = {
    name: string;
    description: string;
    required?: boolean;
    choices?: OptionChoices[];
    type: OptionType;
    exec?: Run
}

type OptionChoices = {
    name: string;
    value: string;
}

export class OptionBuilder {
    private _name: string;
    private _description;
    private _require?: boolean;
    private _type: OptionType;
    private _choices?: OptionChoices[] = [];
    private _exec?: Run;
    constructor(optionoj: option) {
        this._name = optionoj.name;
        this._description = optionoj.description;
        this._require = optionoj.required;
        this._type = optionoj.type;
        this._choices = optionoj.choices = [];
        this._exec = optionoj.exec;
    }
    public async exec(option: runcm) {
        if (this._type === OptionType.SUB_COMMAND && this._exec) {
            return this._exec(option);
        } else if (this._type === OptionType.SUB_COMMAND) {
            return new MessageBuilder().setContent("This command has no execute function")
        }
    }
    get name() {
        return this._name;
    }
    get description() {
        return this._description;
    }
    get require() {
        return this._require;
    }
    get choices() {
        return this._choices;
    }
    get toJSON() {
        return {
            name: this.name,
            description: this.description,
            required: this.require,
            choices: this.choices,
            type: this._type
        }
    }
}

export class Cmd {
    private _name: string;
    private _description: string;
    private _option?: OptionBuilder[] = [];
    private _exec?: Run;
    constructor(cmdOj: cmdSm) {
        this._name = cmdOj.name;
        this._description = cmdOj.description;
        this._option = cmdOj.option;
        this._exec = cmdOj.exec;
    }

    public async exec(option: runcm): Promise<any> {
        if (this._exec === undefined) {
            return new MessageBuilder().setContent("No execute function for this command").toJSON;
        } else {
            const result = await this._exec(option);
            return result.toJSON;
        }
    }


    get toJSON() {
        return {
            name: this.name,
            description: this.description,
            options: this._option?.map(op => op.toJSON),
            type: 1
        }
    }
    get name() {
        return this._name;
    }
    get description() {
        return this._description;
    }

}