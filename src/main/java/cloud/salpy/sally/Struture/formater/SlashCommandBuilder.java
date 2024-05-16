package cloud.salpy.sally.Struture.formater;

import net.dv8tion.jda.api.interactions.DiscordLocale;
import net.dv8tion.jda.api.interactions.commands.DefaultMemberPermissions;
import net.dv8tion.jda.api.interactions.commands.build.SubcommandData;

import java.util.*;

public abstract class SlashCommandBuilder {
    public String parent;
    public String description;
    public List<String> guildid = new ArrayList<>();
    public List<SubCommandBuilder> subcommandDataList = new ArrayList<>();
    public Map<DiscordLocale,String> localeNamemap = new HashMap<>();
    public List<SubcommandData> getSubCommands() {
        List<SubcommandData> data = new ArrayList<>();
        for (SubCommandBuilder scbuidler : subcommandDataList) {
            data.add(scbuidler.build());
        }
        return data;
    }
    public DefaultMemberPermissions defaultMemberPermissions;
    public void setGuildid(String... guild) {
        Collections.addAll(guildid, guild);
    }
    public void addSubcommand(SubCommandBuilder... subcommand) {
        Collections.addAll(subcommandDataList, subcommand);
    }
}
