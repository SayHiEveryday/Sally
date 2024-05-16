package cloud.salpy.sally.Struture.entities;

import club.minnced.discord.webhook.WebhookClient;
import club.minnced.discord.webhook.WebhookClientBuilder;
import java.util.concurrent.ExecutionException;

public class WebhookLog
{
    public enum Level
    {
        INFO("\u2139"), WARNING("\u26A0"), ERROR("\uD83D\uDE31"); // ℹ, ⚠, 😱

        private final String emoji;

        private Level(String emoji)
        {
            this.emoji = emoji;
        }
    }

    private final WebhookClient client;
    private final String logname;

    public WebhookLog(String webhookUrl, String logname)
    {
        this.client = new WebhookClientBuilder(webhookUrl).build();
        this.logname = logname;
    }

    public void send(Level level, String message)
    {
        client.send(level.emoji + " `[" + logname + "]` " + message);
    }

    public void sendBlocking(Level level, String message) throws InterruptedException, ExecutionException
    {
        client.send(level.emoji + " `[" + logname + "]` " + message).get();
    }
}