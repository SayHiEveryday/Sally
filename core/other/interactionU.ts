import { interaction } from "../format/object/interactions";
import { user } from "../format/object/user";
import { Snowflake } from "./snowflake";

export class interactionUtils {
    static getCreatedTimestamp(interaction: interaction) {
        return Number(new Snowflake(interaction.id).timestamp)
    }
    static get(interaction:interaction,name:string) {
        if (interaction.data === undefined) {
            throw new Error("data not found");
        } 
        if (interaction.data.options === undefined) {
            throw new Error("Option not found");
        }
        return interaction.data.options.find(op => op.name === name)?.value ?? undefined;
    }
    static getUser(interaction: interaction,name: string) {
        if (interaction.data === undefined) {
            throw new Error("data not found");
        } 
        if (interaction.data.options === undefined) {
            throw new Error("Option not found");
        }
        if (interaction.data.options.find(op => op.name === name)?.value === undefined) {
            throw new Error("Option name not found");
        }
        return interaction.data.resolved?.users[interaction.data.options.find(op => op.name === name)?.value!] ?? undefined;
    }
}