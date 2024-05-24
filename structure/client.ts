import { Cmd } from "./format/command";
import { interaction } from "./format/object/interactions";
import { MessageBuilder } from "./builder/message";
import { InteractionResponseType } from "discord-interactions";
import { appid, token } from "../constant.json";
import axios from "axios"

export class Client {
    command: Map<string,Cmd> = new Map();

    constructor() {
        
    }

    public runCmd(interaction: interaction) {
        const i: interaction = interaction;
        if (i.data === undefined) {
            return new MessageBuilder().setContent(`Error while trying to call a command`).toJSON;
        }
        if (i.data.name === undefined) {
            return new MessageBuilder().setContent(`Error command ${i.data.name} Not found`).toJSON;
        }
        const cmd = this.command.get(i.data.name);
        if (cmd) {
            const asd = cmd.exec({interaction: i});
            return {
                type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                data: asd
            }
        } else {
            console.error(i.data.name + "not found")
        }
    }
    public regis() {
        this.command.forEach(c => {
            const url = "https://discord.com/api/v10";
            axios.post(url + `/applications/${appid}/commands`, JSON.stringify(c.toJSON), {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bot ${token}`
                }
            }).then(res => {
                if (res.status === 201) {
                    console.log(`Registered ${c.name}`)
                } else {
                    console.log(`Command ${c.name} already registered`)
                }
            });
        });
    }
    public addCommand(c:Cmd) {
        this.command.set(c.name,c);
    }
}