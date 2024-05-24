type EmbedFooter = {
    text: string;
    icon_url?: string;
    proxy_icon_url?: string;
}

type EmbedImage = {
    url: string;
    proxy_url?: string;
    height?: number;
    width?: number;
}

type EmbedThumbnail = {
    url: string;
    proxy_url?: string;
    height?: number;
    width?: number;
}

type EmbedVideo = {
    url: string;
    proxy_url?: string;
    height?: number;
    width?: number;
}

type EmbedProvider = {
    name?: string;
    url?: string;
}

type EmbedAuthor = {
    name: string;
    url?: string;
    icon_url?: string;
    proxy_icon_url?: string;
}

type EmbedField = {
    name: string;
    value: string;
    inline?: boolean;
}


export class EmbedBuilder {
    private title?: string;
    private type: string = "rich"
    private description?: string;
    private url?: string;
    private timestamp?: string;
    private color?: number;
    private footer?: EmbedFooter;
    private image?: EmbedImage;
    private thumbnail?: EmbedThumbnail;
    private video?: EmbedVideo;
    private provider?: EmbedProvider;
    private author?: EmbedAuthor;
    private field: EmbedField[] = [];

    setTitle(title: string) { this.title = title; return this; } 
    setDescription(description: string) { this.description = description; return this; }
    setType(type: string) { this.type = type; return this; }
    setUrl(url:string) { this.url = url; return this; }
    setTimestamp(time: string ) { this.timestamp = time; return this;}
    setColor(color:number) { this.color = color; return this; }
    setFooter(footer: EmbedFooter) { this.footer = footer; return this;}
    setImage(image: EmbedImage) { this.image = image; return this; }
    setThumbnail(thumbnail: EmbedThumbnail) { this.thumbnail = thumbnail; return this;}
    setVideo(video: EmbedVideo) { this.video = video; return this;}
    setProvider(provider: EmbedProvider) { this.provider = provider; return this; }
    setAuthor(author: EmbedAuthor) { this.author = author; return this;}
    addField(field: EmbedField) { field.inline = field.inline ? field.inline : false; this.field?.push(field); return this;}

    get toJSON() {
        return {
            title: this.title,
            description: this.description,
            footer: this.footer,
            author: this.author,
            color: this.color,
            url: this.url,
            type: this.type,
            timestamp: this.timestamp,
            thumbnail: this.thumbnail,
            video: this.video,
            provider: this.provider,
            field: this.field
        }
    }
}