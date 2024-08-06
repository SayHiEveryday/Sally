export class Snowflake {
    private _snowflake: bigint;

    constructor(snowflake: string | Snowflake) {
        if(snowflake instanceof Snowflake) {
            this._snowflake = snowflake.valueOf();
        } else this._snowflake = BigInt(snowflake ?? 0);
    }

    get value() {
        return this._snowflake;
    }

    get timestamp() {
        return (this._snowflake >> 22n) + 1420070400000n;
    }

    get worker() {
        return (this._snowflake & 0x3E0000n) >> 17n;
    }

    get process() {
        return (this._snowflake & 0x1F000n) >> 12n;
    }

    get increment() {
        return this._snowflake & 0xFFFn;
    }

    valueOf() {
        return this._snowflake;
    }

    toString() {
        return this.valueOf().toString();
    }
}