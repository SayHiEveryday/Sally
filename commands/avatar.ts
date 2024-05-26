import {Cmd, OptionBuilder, OptionType} from "../core/format/command";
import {interactionUtils} from "../core/other/interactionU";
import {MessageBuilder} from "../core/builder/message";
import {EmbedBuilder} from "../core/builder/embed";
import {ButtonBuilder, ButtonStyle} from "../core/format/object/component";

export default new Cmd({
    name: "avatar",
    description: "Get avatar from user",
    option: [
        new OptionBuilder({
            name: "member",
            description: "Target Member",
            type: OptionType.USER
        })
    ],
    exec: async ({ interaction }) => {
        let member: any;
        // try {
        //     member = interaction.data?.resolved?.users[interaction.data?.options!.find(op => op.name === "member")!.value]
        // } catch (e) {
        //     member = interaction.member!.user;
        // }
        if (interaction.data?.resolved === undefined) {
            member = interaction.member!.user
        } else {
            member = interaction.data?.resolved?.users[interaction.data?.options!.find(op => op.name === "member")!.value]
        }
        return new MessageBuilder()
            .setContent(`https://cdn.discordapp.com/avatars/${member.id}/${member.avatar}?size=1024`)
            .addButton(new ButtonBuilder({
                label: "WEBP",
                custom_id: "userinfo:Webp",
                style: ButtonStyle.Primary,
                exec: async ({ interaction }) => {
                    return new MessageBuilder()
                        .setContent(`https://cdn.discordapp.com/avatars/${member.id}/${member.avatar}.webp?size=1024`)
                        .setEphermal(true);
                }
            })).addButton(new ButtonBuilder({
                label: "PNG",
                custom_id: "userinfo:Png",
                style: ButtonStyle.Primary,
                exec: async ({ interaction }) => {
                    return new MessageBuilder()
                        .setContent(`https://cdn.discordapp.com/avatars/${member.id}/${member.avatar}.png?size=1024`)
                        .setEphermal(true);
                }
            })).addButton(new ButtonBuilder({
                    label: "JPEG",
                    custom_id: "userinfo:JPEG",
                    style: ButtonStyle.Primary,
                    exec: async ({ interaction }) => {
                        return new MessageBuilder()
                            .setContent(`https://cdn.discordapp.com/avatars/${member.id}/${member.avatar}.jpeg?size=1024`)
                            .setEphermal(true);
                    }
            }))
    }
})