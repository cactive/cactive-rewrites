import { parse } from "ts-command-line-args";

import Arguments from "./types/arguments";

import { self, retrieve } from "./ip";

function test(a: string, b: string) {
    console.log(a, b)
}

const year = new Date().getFullYear();
const valid_modules: string[] = [
    "ip",
];
const valid_functions: {[k: string]: string[]} = {
    "ip": [
        "self",
        "retrieve",
    ],
};
const modules_functions_mapping: {[k: string]: {[k: string]: (...args: any[]) => any | void | Promise<any> | Promise<void>}} = {
    "ip": {
        self,
        retrieve,
    },
};
const args = parse<Arguments>(
    {
        module: { type: String, alias: "m", description: "The Cactive module to use (ip, etc.)" },
        func: { type: String, alias: "f", description: "The function to use from that module (retrieve, etc.)" },
        args: { type: String, optional: true, alias: "a", description: "The args to pass to that function seperated by ',' ('8.8.8.8, hi')" },
        help: { type: Boolean, optional: true, alias: "h", description: "Prints the usage guide" },
    },
    {
        helpArg: "help",
        headerContentSections: [{ header: "Cactive Bin Config", content: "By using Cactive Bin, you agree to our CactiveNetwork Licence Version 1.0" }],
        footerContentSections: [{ header: `Copyright © ${year} Luke Matison, Cactive.`, content: "All Rights Reserved." }],
    },
);

if (!args.help) {
    if (!valid_modules.includes(args.module)) throw Error("That is not a valid module!");
    if (!valid_functions[args.module].includes(args.func)) throw Error("That is not a valid function for that module!");

    // Load Module's Function With Args
    let pass_args: string[];
    if (args.args) {
        pass_args = args.args.replace(" ", "").split(",");
    } else {
        pass_args = [];
    }

    if (pass_args.length < modules_functions_mapping[args.module][args.func].length) throw Error("User passed too little arguments for that function");

    (async () => {
        await modules_functions_mapping[args.module][args.func](...pass_args);
    })().catch(e => {
        console.log(e);
    });
}