import { client } from "../..";
import { ActionRowBuilder, ButtonBuilder, ButtonStyle } from "../format/object/component";
import { EmbedBuilder } from "./embed";

export class MessageBuilder {
    private content?: string;
    private embeds?: Array<EmbedBuilder> = [];
    private ephermal: boolean = false;
    private buttons?: ButtonBuilder[] = [];
    constructor() {

    }
    public setContent(content: string) {
        this.content = content;
        return this;
    }
    public addEmbed(embed: EmbedBuilder) {
        this.embeds?.push(embed);
        return this;
    }
    public addButton(op: ButtonBuilder) {
        if (op.Style !== ButtonStyle.Link) {
            if (op.custom_ID === undefined) {
                throw new Error("Custom id can't be null if button isn't link")
            }
            client.button.set(op.custom_ID,op);
        }
        this.buttons?.push(op);
        return this;

    }
    public setEphermal(eph: boolean) {
        this.ephermal = eph
        return this;
    }
    get Ephermal() {
        if (this.ephermal) {
            return 64;
        } else {
            return 0
        }
    }
    get toJSON() {
        let actionrow = new ActionRowBuilder()
        if (this.buttons !== undefined && this.buttons.length !== 0) {
            this.buttons?.forEach((button) => {
                actionrow.addButton(button)
            })
        }
        let as: any  = {
            content: this.content,
        }
        if (this.embeds) {
            as["embeds"] = this.embeds.map(embed => embed.toJSON);
        }
        if (this.ephermal) {
            as["flags"] = this.Ephermal;
        }
        if ( this.buttons !== undefined && this.buttons.length !== 0 ) {
            as["components"] = [actionrow.toJSON]
        }
        return as;
    }
}