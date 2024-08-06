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
    type: ChannelType;
}

export enum ChannelType {
    GUILD_TEXT,
    DM,
    GUILD_VOICE,
    GROUP_DM,
    GUILD_CATEGORY,
    GUILD_ANNOUNCEMENT,
    ANNOUNCEMENT_THREAD = 10,
    PUBLIC_THREAD,
    PRIVATE_THREAD,
    GUILD_STAGE_VOICE,
    GUILD_DIRECTORY,
    GUILD_FORUM,
    GUILD_MEDIA,

}