export type channel = {
    flags: number;
    guild_id: string;
    id: string;
    last_message_id: string;
    name: string;
    nsfw: boolean;
    parent_id: string | undefined;
    permission: string;
    possition: number;
    rate_limit_per_user: number;
}