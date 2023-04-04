---
layout: ../../layouts/MarkdownPostLayout.astro
title: "How to Remap the F4 Key on M1 Macs to Something Else Than Spotlight"
date: 2022-01-23
tags: ["macOS"]
summary: "Learn how to remap the F4 key to Alfred or Raycast"
---
I don't use Spotlight anymore for many years already. I don't find it fast enough and the way it keeps re-organizing the results all the time makes me miss often what I want to select. I used to use [Alfred](https://www.alfredapp.com) instead, but I started using [Raycast](https://raycast.com) a few months ago and sticked with it so far.

Fast forward to last week, I finally received my new M1 Pro MacBook Pro and it has the new keyboard layout that Apple is progressively bringing to its laptop range.

![The new keyboard (source *Apple*)](/images/2022-01-23-keyboard.png)

The F4 key on the new layout allows to quickly[1] access Spotlight. Logically, I wanted to replace this with Raycast and found it very easy to do using [Karabiner](https://karabiner-elements.pqrs.org).

To install it, just run `brew install karabiner-elements`.

After the initial launch, I just had to add the following section in the config file `~/.config/karabiner/karabiner.json` (under `profiles/fn_function_keys`):

```json
{
    "from": {
        "key_code": "f4"
    },
    "to": [
        {
            "shell_command": "open -a '/Applications/Raycast.app'"
        }
    ]
}
```

[1]: even though I guess nothing beats the speed of "⌘ + space" for me