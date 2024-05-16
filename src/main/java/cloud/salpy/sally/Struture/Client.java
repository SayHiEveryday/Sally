package cloud.salpy.sally.Struture;

import cloud.salpy.sally.Struture.entities.WebhookLog;
import cloud.salpy.sally.pri.Constant;
import net.dv8tion.jda.api.JDA;
import net.dv8tion.jda.api.JDABuilder;
import net.dv8tion.jda.api.hooks.ListenerAdapter;
import net.dv8tion.jda.api.requests.GatewayIntent;
import net.dv8tion.jda.api.sharding.ShardManager;
import net.dv8tion.jda.api.utils.MemberCachePolicy;

public class Client {
    private final JDABuilder jdaBuilder;
    public ShardManager shardManager;
    public WebhookLog webhook;

    public Client(String token) {
        this.jdaBuilder = JDABuilder.createLight(token)
                .setMemberCachePolicy(MemberCachePolicy.ALL)
                .enableIntents(GatewayIntent.getIntents(GatewayIntent.ALL_INTENTS));
        this.webhook = new WebhookLog(Constant.webhookurl,"Client");
    }
    public void addEvent(ListenerAdapter listenerAdapter) {
        this.jdaBuilder.addEventListeners(listenerAdapter);
    }
    public JDA build() {
        return this.jdaBuilder.build();
    }
}
