import { parse } from "ts-command-line-args";
import { readFileSync, existsSync } from "fs";
import { createInterface } from "readline";

import Arguments from "./types/arguments";
import Cactive from "./types/cactive";
import Input from "./types/input";

import { self, retrieve } from "./ip";

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
        file: { type: String, alias: "f", defaultValue: "cactive.json", description: "The file location of you cactive.json file" },
        help: { type: Boolean, optional: true, alias: "h", description: "Prints the usage guide" },
    },
    {
        helpArg: "help",
        headerContentSections: [{ header: "Cactive Bin Config", content: "By using Cactive Bin, you agree to our CactiveNetwork Licence Version 1.0" }],
        footerContentSections: [{ header: `Copyright © ${year} Cactive.`, content: "All Rights Reserved." }],
    },
);

if (!args.help) {
    if (!existsSync(args.file)) throw Error("Your file has to exist!");

    const rl = createInterface({
        input: process.stdin,
        output: process.stdout,
    });
    const question = (questionText: string) => new Promise<string>(resolve => rl.question(questionText, resolve));

    let cactiveFile: Cactive;

    try {
        cactiveFile = JSON.parse(readFileSync(args.file, 'utf-8'));
    } catch (e) {
        throw Error("Your file has to be JSON parsable!");
    }

    (async() => {
        while (true) {
            let input: Input;
            try {
                input = JSON.parse(await question(">>> "));
            } catch (e) {
                throw Error("Input must be JSON parsable!");
            }

            if (!cactiveFile[input.command]) throw Error(`Command ${input.command} was not found in your cactive.json!`);

            const command = cactiveFile[input.command];
            let args: any[];
            let module = command.module;

            if (!valid_modules.includes(module)) throw Error(`Module ${module} is not a valid module!`);
            if (!valid_functions[module].includes(command.func)) throw Error(`Function ${command.func} is not a valid function for module ${command.module}!`);

            if (command.args === "user") {
                if (!input.args) throw Error("Arguments are required on a user args command!");

                args = Object.values(input.args);
            } else {
                args = Object.values(command.args);
            }

            const func = modules_functions_mapping[command.module][command.func];

            if (args.length < func.length || args.length > func.length) throw Error("You passed too little or too many arguments for that function!");

            try {
                await func(...args);
            } catch (e) {
                console.log(e);
            }
        }
    })();
}