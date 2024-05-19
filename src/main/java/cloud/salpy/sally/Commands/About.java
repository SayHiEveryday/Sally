package cloud.salpy.sally.Commands;

import cloud.salpy.sally.Structure.Client;
import com.jagrosh.interactions.command.ApplicationCommand;
import com.jagrosh.interactions.entities.SentMessage;
import com.jagrosh.interactions.receive.Interaction;
import com.jagrosh.interactions.responses.InteractionResponse;
import com.jagrosh.interactions.responses.MessageCallback;

public class About extends command {
    public About(Client bot) {
        super(bot);
        this.app = new ApplicationCommand.Builder()
                .setType(ApplicationCommand.Type.CHAT_INPUT)
                .setName("s!about")
                .setDescription("Show About bot")
                .setDmPermission(true)
                .build();

    }
    @Override
    protected InteractionResponse Execute(Interaction interaction) {
        return new MessageCallback(new SentMessage.Builder().setContent("Test").build());
    }
}
