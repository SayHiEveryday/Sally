import axios from "axios";
import { EmbedBuilder } from "../core/builder/embed";
import { MessageBuilder } from "../core/builder/message";
import { Cmd } from "../core/format/command";
import { InteractionContextTypes } from "../core/format/object/interactions";
import { guild_cache } from "../utils/cache/guilds";
import { token } from "../constant.json"

export default new Cmd({
    name: "serverinfo",
    description: "Current Server Infomation",
    exec: ({ interaction }) => {
        if (interaction.context !== InteractionContextTypes.GUILD) {
            const embed = new EmbedBuilder()
                .setColor(0xFFFFFF)
                .setTitle(":x: Error")
                .setDescription("Cannot use this command in dm")
            return new MessageBuilder().addEmbed(embed).setEphermal(true)
        }
        if (interaction.guild === undefined) {
            return new MessageBuilder().setContent("Error while fetching guild").setEphermal(true)
        }
        const guild = guild_cache.get(interaction.guild.id);
        let g;
        if (guild === undefined) {
            axios.get("https://discord.com/api/v10/guilds/1213461528611790848",{
                headers: {
                    Authorization: `Bot ${token}`
                }
            }).then(res => {
                JSON.parse(res.data)
            })
        }
        return new MessageBuilder()
            .setContent(g ?? "undefined")
            .setEphermal(true)
    }
})