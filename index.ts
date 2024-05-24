import { InteractionType, verifyKeyMiddleware } from "discord-interactions";
import express from "express";
import { publickey } from "./constant.json";
import { Client } from "./structure/client";
import ping from "./commands/ping";
import userinfo from "./commands/userinfo";
import serverinfo from "./commands/serverinfo";


const app = express();
const client = new Client();
client.addCommand(ping)
client.addCommand(userinfo)
client.addCommand(serverinfo)

// app.use(bodyParser.json())

app.post("/interactions",verifyKeyMiddleware(publickey), async (req,res) => {
    const interaction = req.body;
    if (interaction.type == InteractionType.APPLICATION_COMMAND) {
        const a = client.runCmd(interaction);
        res.json(a);
    }
});

client.regis()

app.listen(5000);