package cloud.salpy.sally.Commands.Bot;

import cloud.salpy.sally.Struture.formater.SubCommandBuilder;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.interactions.DiscordLocale;

public class Ping extends SubCommandBuilder {
    public Ping() {
        this.name = "ping";
        this.description = "Return latency between bot and discord";
        this.localeNamemap.put(DiscordLocale.THAI,"ปิง");
    }
    @Override
    public void execute(SlashCommandInteractionEvent event) {
        event.reply("Pong! Gateway Latency is `" + event.getJDA().getGatewayPing() + "` ms").queue();
    }
}
