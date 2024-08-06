import {EmbedBuilder} from "../core/builder/embed";
import {MessageBuilder} from "../core/builder/message";
import {Cmd} from "../core/format/command";
import {InteractionContextTypes} from "../core/format/object/interactions";
import {guild_cache} from "../utils/cache/guilds";
import {ButtonBuilder, ButtonStyle} from "../core/format/object/component";
import axios from "axios";
import { token } from "../constant.json";
import {guild} from "../core/format/object/guild";
import {Snowflake} from "../core/other/snowflake";

export default new Cmd({
    name: "serverinfo",
    description: "Current Server Infomation",
    exec: async ({ interaction }) => {
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

        const result = await axios.get("https://discord.com/api/v10/guilds/" + interaction.guild.id + "?with_counts=1", {
            headers: {
                Authorization: `Bot ${token}`
            }
        })
        const g: guild = result.data;
        const embed = new EmbedBuilder()
            .setColor(0xFFFFFF)
            .setDescription(" "
                + `Name: ${g.name}\n`
                + `Owner: <@${g.owner_id}>\n`
                + `Created at: <t:${new Snowflake(g.id).timestamp}:F>\n`
                + `Max Member: ${g.max_members}\n`
                + `Member Count: ${g.approximate_member_count}`
            )
            .setFooter({ text: `ID: ${g.id}` })
        if (g.icon !== undefined) {
            embed.setThumbnail({
                url: `https://cdn.discordapp.com/icons/${g.id}/${g.icon}`
            })
        }
        if (g.banner !== null) {
            embed.setImage({
                url: `https://cdn.discordapp.com/banners/${g.id}/${g.banner}?size=1024`
            })
        }
        return new MessageBuilder()
            .addEmbed(embed)
    }
})