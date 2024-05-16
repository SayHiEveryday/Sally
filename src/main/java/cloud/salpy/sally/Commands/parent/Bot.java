package cloud.salpy.sally.Commands.parent;

import cloud.salpy.sally.Commands.Bot.Ping;
import cloud.salpy.sally.Struture.formater.SlashCommandBuilder;
import net.dv8tion.jda.api.interactions.DiscordLocale;

public class Bot extends SlashCommandBuilder {
    public Bot() {
        this.parent = "bot";
        this.description = "Bot parent";
        this.localeNamemap.put(DiscordLocale.THAI,"บอท");
        this.addSubcommand(
                new Ping()
        );
    }
}
