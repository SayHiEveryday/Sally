import { MessageBuilder } from "../core/builder/message";
import { Cmd, OptionBuilder, OptionType } from "../core/format/command";
import { interactionUtils } from "../core/other/interactionU";

export default new Cmd({
    name: "userinfo",
    description: "User infomation",
    option: [
        new OptionBuilder({
            name: "member",
            description: "Target Member",
            required: false,
            type: OptionType.USER
        }),
    ],
    exec: async ({ interaction }) => {
        if (interaction.data?.resolved === undefined) {
            member = interaction.member!.user
        } else {
            member = interaction.data?.resolved?.users[interaction.data?.options!.find(op => op.name === "member")!.value]
        }

        const message = new MessageBuilder().setContent(`https://cdn.discordapp.com/avatars/${member?.id}/${member?.avatar}.png?size=1024`);
        return message
    }
})