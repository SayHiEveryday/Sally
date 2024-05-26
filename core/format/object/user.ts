type avatar_decoration = {
    asset: string;
    sku_id: string | number
}
export type user = {
    avatar: string | undefined;
    avatar_decoration_data: avatar_decoration | undefined;
    discriminator: string;
    global_name: string;
    id: string;
    public_flags: number;
    username: string;
}