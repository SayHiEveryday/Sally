import { MessageBuilder } from "../structure/builder/message";
import { Cmd, OptionBuilder, OptionType } from "../structure/format/command";
import { interactionUtils } from "../structure/other/interactionU";

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
    exec: ({ interaction }) => {
        const member = interactionUtils.getUser(interaction,"member");
        const message = new MessageBuilder().setContent(`https://cdn.discordapp.com/avatars/${member?.id}/${member?.avatar}.png?size=1024`);
        return message
    }
})