### What is this?
This is CAP or Cactive's Assembled Packages. In short, it is a compiled NodeJS script that allows you to use Cactive's products from any coding language or without one at all!

### How do I set it up?
First, install the cactive-bin.zip file from the most recent release

Extract that zip file

Now in the same directory as the cactive-bin extracted folder, open cmd

Now execute the correct file and add a -h (help) flag. For example, on Windows:
```bash
.\cactive-bin\cactive-bin-win.exe -h
```

### cactive.json File
The Cactive JSON file's location is specified using the -f flag and defaults to "./cactive.json"

The file contains special commands that hold which module, function, and args to pass. For example:
```json
{
  "retrieve": {
    "module": "ip",
    "func": "retrieve",
    "args": "user"
  },
  "google": {
    "module": "ip",
    "func": "retrieve",
    "args": {
      "ip": "8.8.8.8"
    }
  }
}
```

Here we define two commands, "retrieve" and "google". The "module" specifies that we will run a command from Cactive's IP Module. "func" specifies that we will run the "retrieve" function from Cactive's IP Module. Args specifies two different things, it specifies for "retrieve", we will let the user decide the args to be passed. For "google", it specifies
the arguments passed to the function will always be {"ip": "8.8.8.8"}.

To use this file we can run our cactive-bin program and we can do something like this where the text after ">>> " is stringified JSON
```bash
>>> {"command":"google"}
[output here]
>>> {"command":"retrieve","args":{"ip":"8.8.8.8"}}
```

The data after ">>> " is just stringified JSON that matches this style:
```json
{
    "command": "command to execute from cactive.json",
    "args?": "args to pass to the function defined in cactive.json"
}
```