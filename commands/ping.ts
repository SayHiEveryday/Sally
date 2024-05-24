import { EmbedBuilder } from "../structure/builder/embed";
import { MessageBuilder } from "../structure/builder/message";
import { Cmd } from "../structure/format/command";
import { Snowflake } from "../structure/other/snowflake";


export default new Cmd({
    name: "ping",
    description: "pong",
    exec: ({ interaction }) => {
        return new MessageBuilder()
                    .addEmbed(new EmbedBuilder().setDescription(`Pong! My latency is ${Date.now() - Number(new Snowflake(interaction.id).timestamp)}ms`).setColor(0xFFFFFF));
    }
})