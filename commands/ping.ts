import { EmbedBuilder } from "../core/builder/embed";
import { MessageBuilder } from "../core/builder/message";
import { Cmd } from "../core/format/command";
import { Snowflake } from "../core/other/snowflake";


export default new Cmd({
    name: "ping",
    description: "pong",
    exec: ({ interaction }) => {
        return new MessageBuilder()
                    .addEmbed(new EmbedBuilder().setDescription(`Pong! My latency is ${Date.now() - Number(new Snowflake(interaction.id).timestamp)}ms`).setColor(0xFFFFFF));
    }
})