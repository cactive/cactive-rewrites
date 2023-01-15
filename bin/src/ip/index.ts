import phin from "phin";

const fetch = async (ip: string | null): Promise<void> => {
    const { body }: any = await phin({
        url: `https://ip.cactive.co/api/lookup/${ip ?? ''}`,
        method: "GET",
        parse: "json",
    }).catch((error) => {
        throw new Error(error);
    });
    
    if (body.errors) throw new Error(body.errors[0].message);
    console.log(JSON.stringify(body));
}
    
export const self = (): Promise<void> => fetch(null);
export const retrieve = (ip: string): Promise<void> => fetch(ip);