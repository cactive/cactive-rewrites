type args = "user";

export default interface Cactive {
    [k: string]: {
        module: string
        func: string
        args: args | {[k: string]: any}
    }
}