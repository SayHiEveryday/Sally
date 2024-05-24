export type role = {
    id: string,
    name: string,
    color: number,
    hoist: boolean,
    icon?: string,
    unicode_emoji?: string,
    position: number,
    permissions: string,
    managed: boolean,
    mentionable: boolean,
    flags: number,
    tags: roleTags
}

type roleTags = {
    bot_id?: string,
    integration_id?: string,
    premium_subscriber?: boolean,
    subscription_listing_id?: string,
    available_for_purchase?: boolean,
    guild_connections?: boolean
}