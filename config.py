from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session1 = os.environ.get("TERMUX")
SESSION1 = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")
DEVLOO = os.environ.get("DEVLO")

sython1 = TelegramClient(StringSession(session1), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)


session2 = os.environ.get("TERMUXX")
SESSION2 = os.environ.get("TERMUXX")
sython2 = TelegramClient(StringSession(session2), APP_ID, APP_HASH)


session3 = os.environ.get("TERMUXXX")
SESSION3 = os.environ.get("TERMUXXX")
sython3 = TelegramClient(StringSession(session3), APP_ID, APP_HASH)


session4 = os.environ.get("TERMUXXXX")
SESSION4 = os.environ.get("TERMUXXXX")
sython4 = TelegramClient(StringSession(session4), APP_ID, APP_HASH)


session5 = os.environ.get("TERMUXXXXX")
SESSION5 = os.environ.get("TERMUXXXXX")
sython5 = TelegramClient(StringSession(session5), APP_ID, APP_HASH)



ispay = ['yes']
ispay2 = ['yes']
bot.start()
