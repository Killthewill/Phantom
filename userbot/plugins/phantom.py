"""Emoji

Available Commands:

.phantom"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("phantom"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "phantom":
    await event.edit("phantom")
    animation_chars = [
            "Phantom",
            "pHantom",
            "phAntom",
           "phaNtom",
            "phanTom",
            "phantOm",
            "phantoM",
            "PhAnToM",
            "PHANTOM",
            "@PhantomBots"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
