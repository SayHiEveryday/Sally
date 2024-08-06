import { promises } from "fs";
import path from "path";

export class fileRead {
    public async import(path: any) {
        return (await import(path))?.default;
    };

    public async read(dir: any) {
        let files: any = [];
        const dirents = await promises.readdir(dir, { withFileTypes: true });

        for (const dirent of dirents) {
            const res = path.resolve(dir, dirent.name);
            if (dirent.isDirectory()) {
                files = [...files, ...await new fileRead().read(res)];
            } else if (dirent.isFile() && dirent.name.endsWith(".ts")) {
                files.push(res);
            }
        }
        
        return files;
    }
}