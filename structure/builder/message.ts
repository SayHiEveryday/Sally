import { EmbedBuilder } from "./embed";

export class MessageBuilder {
    private content?: string;
    private embeds?: Array<EmbedBuilder> = new Array();
    private ephermal: boolean = false;
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
    public setEphermal(eph: boolean) {
        this.ephermal = eph
        return this;
    }
    get Ephermal() {
        if (this.ephermal === true) {
            return 64;
        } else {
            return 0
        }
    }
    get toJSON() {
        return {
            content: this.content,
            embeds: this.embeds?.map(embed => embed.toJSON),
            flags: this.Ephermal
        }
    }
}