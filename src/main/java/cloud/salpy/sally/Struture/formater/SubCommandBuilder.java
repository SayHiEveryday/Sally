package cloud.salpy.sally.Struture.formater;

import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.interactions.DiscordLocale;
import net.dv8tion.jda.api.interactions.commands.build.OptionData;
import net.dv8tion.jda.api.interactions.commands.build.SubcommandData;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public abstract class SubCommandBuilder {
    public String name;
    public String description;
    public List<OptionData> optionData = new ArrayList<>();
    public Map<DiscordLocale,String> localeNamemap = new HashMap<>();
    public abstract void execute(SlashCommandInteractionEvent event);
    public SubcommandData build() {
        return new SubcommandData(this.name,this.description)
                .setNameLocalizations(localeNamemap)
                .addOptions(optionData);
    }
}
