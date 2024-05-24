import { EmbedBuilder } from "../structure/builder/embed";
import { MessageBuilder } from "../structure/builder/message";
import { Cmd } from "../structure/format/command";
import { InteractionContextTypes } from "../structure/format/object/interactions";
import { guild_cache } from "../utils/cache/guilds";

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
        return new MessageBuilder().setContent("this is a test").setEphermal(true)
    }
})