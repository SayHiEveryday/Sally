import { components } from "./component";
import { embed } from "./embed";
import { interaction } from "./interactions";
import { role } from "./role";
import { user } from "./user";

export type message = {
    attachments?:string[];
    author: user;
    components?: components;
    content?: string;
    edited_timestamp?: string;
    embeds: embed;
    flags: number;
    id: string;
    interaction: interaction;
    mention_everyone: boolean;
    mention_roles: role[];
    mentions: string[];
    pinned: boolean;
    position: number;
    timestamp: string;
    tts: boolean;
    type: number;
    webhook_id?: string;
}