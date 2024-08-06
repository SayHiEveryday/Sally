import { role } from "./role"
import { user } from "./user"

export type emoji = {
    id?: string,
    name?: string,
    roles?: role,
    user?: user,
    require_colons?: boolean,
    managed?: boolean,
    animated?: boolean,
    avaliable?: boolean,
}

export type sticker = {
    id: string;
    pack_id?: string;
    name: string;
    description?: string;
    tags: string;
    asset?: string;
    type: number;
    format_type: number;
    avaliable?: boolean;
    guild_id?: string,
    user?: user,
    sort_value?: number
}