package cloud.salpy.sally.Commands;

import cloud.salpy.sally.Structure.Client;
import com.jagrosh.interactions.command.ApplicationCommand;
import com.jagrosh.interactions.command.Command;
import com.jagrosh.interactions.entities.Guild;
import com.jagrosh.interactions.entities.SentMessage;
import com.jagrosh.interactions.receive.Interaction;
import com.jagrosh.interactions.requests.Route;
import com.jagrosh.interactions.responses.InteractionResponse;
import com.jagrosh.interactions.responses.MessageCallback;
import java.time.Instant;
import java.util.HashSet;
import java.util.Set;
import org.json.JSONObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 *
 * @author John Grosh (john.a.grosh@gmail.com)
 */
public abstract class command implements Command
{
    private final Logger log = LoggerFactory.getLogger(command.class);
    private final Set<Long> currentlyUpdating = new HashSet<>();
    protected final Client bot;
    protected ApplicationCommand app;

    protected command(Client bot)
    {
        this.bot = bot;
    }

    @Override
    public ApplicationCommand getApplicationCommand()
    {
        return app;
    }

    @Override
    public InteractionResponse execute(Interaction interaction)
    {
        // bot cannot be used in DMs
        if(interaction.getGuildId() == 0L)
            return new MessageCallback(new SentMessage.Builder().setContent("This can't be use in dm!").build());

        Instant now = Instant.now();
        long gid = interaction.getGuildId();
        currentlyUpdating.add(gid);
        Guild g;
        try
        {
            JSONObject gjson = bot.getRestClient().request(Route.GET_GUILD.format(gid), "").get().getBody();
            //log.info(String.format("Retrieved guild: " + gjson));
            g = new Guild(gjson);
        }
        catch(Exception ex)
        {
            g = null;
            log.error(String.format("Failed to retrieve guild: %s", ex));
        }
        currentlyUpdating.remove(gid);

        // attempt to run command
        return Execute(interaction);
    }

    protected abstract InteractionResponse Execute(Interaction interaction);

    public static MessageCallback respondSuccess(String content)
    {
        return respond(content);
    }

    public static MessageCallback respondError(String content)
    {
        return respond(":x:" + " " + content);
    }

    public static MessageCallback respond(String content)
    {
        return new MessageCallback(new SentMessage.Builder().setContent(content).setEphemeral(true).build());
    }
}