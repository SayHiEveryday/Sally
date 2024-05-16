package cloud.salpy.sally.Struture.Manager;

import cloud.salpy.sally.Struture.formater.SlashCommandBuilder;
import cloud.salpy.sally.Struture.formater.SubCommandBuilder;
import cloud.salpy.sally.pri.Constant;
import cloud.salpy.sally.Struture.entities.WebhookLog;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.entities.Guild;
import net.dv8tion.jda.api.events.interaction.command.SlashCommandInteractionEvent;
import net.dv8tion.jda.api.events.session.ReadyEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

import org.jetbrains.annotations.NotNull;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class SlashCommandManager extends ListenerAdapter {
    private final List<SlashCommandBuilder> slashCommandBuilders = new ArrayList<>();
    @Override
    public void onReady(ReadyEvent event) {
        JDA jda = event.getJDA();
        for (SlashCommandBuilder scb : slashCommandBuilders) {
            if (scb.guildid.isEmpty()) {
                jda.upsertCommand(scb.parent,scb.description)
                        .setNameLocalizations(scb.localeNamemap)
                        .addSubcommands(scb.getSubCommands())
                        .queue();
            } else {
                for (Guild guild : event.getJDA().getGuilds()) {
                    if (scb.guildid.contains(guild.getId())) {
                        guild.upsertCommand(scb.parent,scb.description)
                                .addSubcommands(scb.getSubCommands())
                                .queue();
                    }
                }
            }
        }
    }

    @Override
    public void onSlashCommandInteraction(@NotNull SlashCommandInteractionEvent event) {
        try {
            for (SlashCommandBuilder scb : slashCommandBuilders) {
                if (scb.parent.equals(event.getName())) {
                    for (SubCommandBuilder scdata : scb.subcommandDataList) {
                        if (scdata.name.equals(event.getSubcommandName())) {
                            scdata.execute(event);
                        }
                    }
                }
            }
        } catch (Exception e) {
            WebhookLog logger = new WebhookLog(Constant.webhookurl,"SlashCommandManager");
            logger.send(WebhookLog.Level.ERROR, Arrays.toString(e.getStackTrace()));
        }
    }

    public void add(SlashCommandBuilder... scb) {
        Collections.addAll(slashCommandBuilders, scb);
    }
    public void add(SlashCommandBuilder scb) {
        slashCommandBuilders.add(scb);
    }
}
