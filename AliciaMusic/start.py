from pyrogram import Client as Aliciabot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from AliciaMusic.config import BOT_NAME as bn, BG_IMAGE




@Aliciabot.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start_(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}![🤓]({BG_IMAGE})
        
I am 𝐀𝐰𝐞𝐬𝐨𝐦𝐞 𝐁𝐥𝐨𝐬𝐬𝐨𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭🎶🎸
I can play songs in your group's VC 🤗
To listen songs add me to your group..
And don't forgot to promote me with all rights!🥰
Otherwise I can't play songs!🥺👉👈
Use the buttons below to know more about me..😊
Add my assistant @A_B_Music_Assistant
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "⚡Commands⚡", url="https://telegra.ph/MUSIC-BOT-COMMANDS-09-28")
                  ],[
                    InlineKeyboardButton(
                        "Owner👑", url="https://t.me/best_friends_official1"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Github🤖", url="https://t.me/H1M4N5HU0P"
                    )],[
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Awesome_blossom_music_bot?startgroup=true"
                    )
                ]
            ]
        ),
    )

@Aliciabot.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(client: Aliciabot, message: Message):
      await message.reply_text("""**𝐀𝐰𝐞𝐬𝐨𝐦𝐞 𝐁𝐥𝐨𝐬𝐬𝐨𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭🎶🎸 is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner👑", url="https://t.me/best_friends_official1")
                ]
            ]
        )
   )


@Aliciabot.on_message(filters.command("help") & filters.private & ~filters.channel)
async def help(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}! [Click here](https://telegra.ph/MUSIC-BOT-COMMANDS-09-28) to know about my Commands.⚡🔥
        """)
        

@Aliciabot.on_message(filters.command("commands") & filters.private & ~filters.channel)
async def commands(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
          message.from_user.mention)}! [Click here](https://telegra.ph/MUSIC-BOT-COMMANDS-09-28) to know about my Commands.⚡🔥
        """)
