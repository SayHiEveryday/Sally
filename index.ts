import { InteractionType, verifyKeyMiddleware } from "discord-interactions";
import express from "express";
import { publickey } from "./constant.json";
import { Client } from "./core/client";
import ping from "./commands/ping";
import userinfo from "./commands/userinfo";
import serverinfo from "./commands/serverinfo";
import avatar from "./commands/avatar";
import Cluster from "node:cluster";
import * as os from "node:os";


const app = express();
export const client = new Client();
client.addCommand(ping)
client.addCommand(userinfo)
client.addCommand(serverinfo)
client.addCommand(avatar)

// app.use(bodyParser.json())
app.post("/interactions",verifyKeyMiddleware(publickey), async (req,res) => {
    const interaction = req.body;
    if (interaction.type === InteractionType.APPLICATION_COMMAND) {
        client.runCmd(interaction).then(result => {
            res.setHeader("X-Powered-By","https://github.com/SayHiEveryday").json(result);
            return;
        });
        return;
    } else if (interaction.type === InteractionType.MESSAGE_COMPONENT) {
        client.runComponents(interaction).then(result => {
           res.setHeader("X-Powered-By","https://github.com/SayHiEveryday").json(result);
           return;
        });
    }
});
if (Cluster.isPrimary) {
    // client.regis()
    console.log(`Primary process: ${process.pid}`);
    const numCPUs = os.cpus().length;

    for (let i = 0; i < numCPUs; i++) {
        Cluster.fork();
    }
    Cluster.on('exit', (worker, code, signal) => {
        console.log(`Worker process ${worker.process.pid} died. Restarting...`);
        Cluster.fork();
    });
} else {
    app.listen(3000, () => {
        console.log(`Starting Bot at ${process.pid}`);
    });
}



