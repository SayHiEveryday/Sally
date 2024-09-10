import { emoji, sticker } from "./emoji";
import { role } from "./role";

enum GuildVerificationLevel {
    NONE = 0,
    LOW = 1,
    MEDIUM = 2,
    HIGH = 3,
    VERY_HIGH = 4,
}

enum DefaultMessageNotificationLevel {
    ALL_MESSAGES = 0,
    ONLY_MENTIONS = 1,
}

enum ExplicitContentFilterLevel {
    DISABLED = 0,
    MEMBERS_WITHOUT_ROLES = 1,
    ALL_MEMBERS = 2,
}

type WelcomeChannel = {
    channel_id: string,
    description: string,
    emoji_id?: string,
    emoji_name?: string 
}

type WelcomeScreen = {
    description?: string,
    welcome_channels: WelcomeChannel
}

export type guild = {
    features: string[];
    id: string;
    locale: string;
    name: string;
    icon?: string;
    icon_hash?: string;
    splash?: string;
    discovery_splash?: string;
    owner_id: string;
    verification_level: GuildVerificationLevel;
    default_message_notifications: DefaultMessageNotificationLevel;
    explicit_content_filter: ExplicitContentFilterLevel;
    roles: role[],
    emojis: emoji[],
    mfa_level: number,
    application_id?: string,
    system_channel_id: string,
    system_channel_flags: number,
    rules_channel_id?: string,
    max_presences?: number,
    max_members?: number,
    vanity_url_code?: string,
    description?: string,
    banner?: string,
    premium_tier: number,
    premium_subscription_count?: number,
    preferred_locale: string,
    public_updates_channel_id?: string,
    max_video_channel_users?: number,
    max_stage_video_channel_users: number,
    approximate_member_count?: number,
    approximate_presence_count?: number,
    welcome_screen?: WelcomeScreen,
    nsfw_level: number,
    stickers?: sticker,
    premium_progress_bar_enabled: boolean,
    safety_alerts_channel_id?: string
}