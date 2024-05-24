import { OptionType } from "../command";
import { channel } from "./channel";
import { guild } from "./guild";
import { member } from "./member";
import { user } from "./user";

export enum InteractionContextTypes {
    GUILD = 0,
    BOT_DM = 1,
    PRIVATE_CHANNEL = 2,
}


type InteractionResolve = {
    members: { [key: string]: member },
    users: { [key: string]: user }
}
type InteractionOption = {
    type: OptionType,
    name: string,
    value: string
}

type data = {
    id: string;
    name: string;
    options?: InteractionOption[]
    resolved?: InteractionResolve;
    type: number;
}

export type interaction = {
    app_permission: string;
    application_id: string;
    channel: channel | undefined;
    context: InteractionContextTypes | number | undefined;
    locale: string;
    data: data | undefined;
    guild: guild | undefined;
    member: member | undefined;
    user?: member["user"];
    token: string;
    type: number;
    version: number;
    id: string;
}