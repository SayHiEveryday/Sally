package cloud.salpy.sally;

import cloud.salpy.sally.Commands.parent.Bot;
import cloud.salpy.sally.Struture.Client;
import cloud.salpy.sally.Struture.Manager.SlashCommandManager;
import cloud.salpy.sally.Struture.entities.WebhookLog;
import cloud.salpy.sally.pri.Constant;

import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.sharding.DefaultShardManagerBuilder;
import net.dv8tion.jda.api.utils.ChunkingFilter;

public class Main {
    public static void main(String[] args) {

        SlashCommandManager slashCommandManager = new SlashCommandManager();
        slashCommandManager.add(
            new Bot()
        );

        Client client = new Client(Constant.token);
        client.addEvent(slashCommandManager);
        JDA jda = client.build();
        client.shardManager = DefaultShardManagerBuilder
                .createLight(Constant.token)
                .setShardsTotal(1)
                .setChunkingFilter(ChunkingFilter.NONE)
                .build();
        client.webhook.send(WebhookLog.Level.INFO,jda.getSelfUser().getName() + " is starting");
    }
}