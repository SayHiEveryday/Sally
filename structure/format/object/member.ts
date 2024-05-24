import { user } from "./user";
export type member = {
    avatar: string | undefined;
    joined_at: string;
    mute: boolean;
    nick: string | undefined;
    pending: boolean;
    permission: string;
    premium_since: string | undefined;
    role: string[];
    communication_disabled_until: string | undefined;
    unusual_dm_activity_until: string | undefined;
    user: user | undefined;
}