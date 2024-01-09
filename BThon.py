from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

# -ل

BThon1.start()
BThon2.start()
BThon3.start()
BThon4.start()
BThon5.start()


c = requests.session()
bot_username = '@EEObot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@TTNBOT'
bot_usernameeee = '@xnsex21bot'
bot_usernameeeee = '@MHDN313bot'

ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [5448642653]




@BThon1.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon1(JoinChannelRequest("@BThon"))
    except BaseException:
        pass
        
@BThon1.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon1(JoinChannelRequest("@eeee4eeee"))
    except BaseException:
        pass
      

@BThon1.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon1(JoinChannelRequest("@K5PKK"))
    except BaseException:
        pass  
        
        
@BThon2.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon2(JoinChannelRequest("@BThon"))
    except BaseException:
        pass
        
@BThon2.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon2(JoinChannelRequest("@eeee4eeee"))
    except BaseException:
        pass
      

@BThon2.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon2(JoinChannelRequest("@K5PKK"))
    except BaseException:
        pass  
        
        
@BThon3.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon3(JoinChannelRequest("@BThon"))
    except BaseException:
        pass
        
@BThon3.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon3(JoinChannelRequest("@eeee4eeee"))
    except BaseException:
        pass
      

@BThon3.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon3(JoinChannelRequest("@K5PKK"))
    except BaseException:
        pass  
        
        
@BThon4.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon4(JoinChannelRequest("@BThon"))
    except BaseException:
        pass
        
@BThon4.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon4(JoinChannelRequest("@eeee4eeee"))
    except BaseException:
        pass
      

@BThon4.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon4(JoinChannelRequest("@K5PKK"))
    except BaseException:
        pass  
        
        
@BThon5.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon5(JoinChannelRequest("@BThon"))
    except BaseException:
        pass
        
@BThon5.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon5(JoinChannelRequest("@eeee4eeee"))
    except BaseException:
        pass
      

@BThon5.on(events.NewMessage)
async def join_channel(event):
    try:
        await BThon5(JoinChannelRequest("@K5PKK"))
    except BaseException:
        pass  
        
        

        
        
        
        
        
@BThon1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@BThon2.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@BThon3.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@BThon4.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@BThon5.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@BThon1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @EEObot - `/point1`
• @A_MAN9300BOT - `/point2`
• @TTNBOT - `/point3`
• @XNSEX21BOT - `/point4`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")

@BThon2.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @EEObot - `/point1`
• @A_MAN9300BOT - `/point2`
• @TTNBOT - `/point3`
• @XNSEX21BOT - `/point4`
• @MHDN313bot - `/point5`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")

@BThon3.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @EEObot - `/point1`
• @A_MAN9300BOT - `/point2`
• @TTNBOT - `/point3`
• @XNSEX21BOT - `/point4`
• @MHDN313bot - `/point5`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")


@BThon4.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @EEObot - `/point1`
• @A_MAN9300BOT - `/point2`
• @TTNBOT - `/point3`
• @XNSEX21BOT - `/point4`
• @MHDN313bot - `/point5`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")

@BThon5.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**〠 اوامر حساب المسؤول

• @EEObot - `/point1`
• @A_MAN9300BOT - `/point2`
• @TTNBOT - `/point3`
• @XNSEX21BOT - `/point4`
• @MHDN313bot - `/point5`
• SEND - `/TEST`
• LEAVE CHANNEL & GROUP - `/lpoint`
• TRANSFER POINT - `/transfer`
• INFO ACCOUNT - `/infoacc`
• JOIN BOT CHANNEL - `/join`**""")





@BThon1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

•بوت تمويل مهدويون - `.تجيع مهدويون `

• فحص السورس      - `.فحص`**""")


@BThon2.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

•بوت تمويل مهدويون - `.تجيع مهدويون `

• فحص السورس      - `.فحص`**""")


@BThon3.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

•بوت تمويل مهدويون - `.تجيع مهدويون `

• فحص السورس      - `.فحص`**""")

@BThon4.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

•بوت تمويل مهدويون - `.تجيع مهدويون `

• فحص السورس      - `.فحص`**""")


@BThon5.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

•بوت تمويل مهدويون - `.تجيع مهدويون `

• فحص السورس      - `.فحص`**""")

@BThon1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗕𝗧𝗛𝗢𝗡    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗗𝗮𝗥𝗞  ※

╰───⌯𝗕𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@BThon1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_username)
    await BThon1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_usernamee)
    await BThon1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_usernameee)
    await BThon1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_usernameeee)
    await BThon1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_username)
    await BThon1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")
    
    
    
@BThon1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_usernamee)
    await BThon1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_usernameee)
    await BThon1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_usernameeee)
    await BThon1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon1.on(events.NewMessage(outgoing=True, pattern=".تجميع مهدويون "))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon1(JoinChannelRequest('BThon'))
    channel_entity = await BThon1.get_entity(bot_usernameeeee)
    await BThon1.send_message(bot_usernameeeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon1.get_messages(bot_usernameeeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon1.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon1(ImportChatInviteRequest(bott))
            msg2 = await BThon1.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon1.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon1.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

##########################################

@BThon2.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):

    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗕𝗧𝗛𝗢𝗡    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗗𝗮𝗥𝗞  ※

╰───⌯𝗕𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@BThon2.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_username)
    await BThon2.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon2.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_usernamee)
    await BThon2.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon2.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_usernameee)
    await BThon2.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon2.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_usernameeee)
    await BThon2.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon2.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_username)
    await BThon2.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")
    
    
    
@BThon2.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_usernamee)
    await BThon2.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon2.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_usernameee)
    await BThon2.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon2.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_usernameeee)
    await BThon2.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon2.on(events.NewMessage(outgoing=True, pattern=".تجميع مهدويون "))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon2(JoinChannelRequest('BThon'))
    channel_entity = await BThon2.get_entity(bot_usernameeeee)
    await BThon2.send_message(bot_usernameeeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon2.get_messages(bot_usernameeeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon2.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon2(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon2.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon2(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon2(ImportChatInviteRequest(bott))
            msg2 = await BThon2.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon2.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon2.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon3.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
	
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗕𝗧𝗛𝗢𝗡    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗗𝗮𝗥𝗞  ※

╰───⌯𝗕𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@BThon3.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_username)
    await BThon3.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon3.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_usernamee)
    await BThon3.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon3.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_usernameee)
    await BThon3.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon3.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_usernameeee)
    await BThon3.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon3.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_username)
    await BThon3.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")
    
    
    
@BThon3.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_usernamee)
    await BThon3.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon3.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_usernameee)
    await BThon3.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon3.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_usernameeee)
    await BThon3.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon3.on(events.NewMessage(outgoing=True, pattern=".تجميع مهدويون "))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon3(JoinChannelRequest('BThon'))
    channel_entity = await BThon3.get_entity(bot_usernameeeee)
    await BThon3.send_message(bot_usernameeeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon3.get_messages(bot_usernameeeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon3.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon3(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon3.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon3(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon3(ImportChatInviteRequest(bott))
            msg2 = await BThon3.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon3.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon3.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon4.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
	
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗕𝗧𝗛𝗢𝗡    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗗𝗮𝗥𝗞  ※

╰───⌯𝗕𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@BThon4.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_username)
    await BThon4.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon4.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_usernamee)
    await BThon4.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon4.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_usernameee)
    await BThon4.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon4.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_usernameeee)
    await BThon4.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon4.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_username)
    await BThon4.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")
    
    
    
@BThon4.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_usernamee)
    await BThon4.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon4.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_usernameee)
    await BThon4.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon4.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_usernameeee)
    await BThon4.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon4.on(events.NewMessage(outgoing=True, pattern=".تجميع مهدويون "))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon4(JoinChannelRequest('BThon'))
    channel_entity = await BThon4.get_entity(bot_usernameeeee)
    await BThon4.send_message(bot_usernameeeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon4.get_messages(bot_usernameeeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon4.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon4(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon4.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon4(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon4(ImportChatInviteRequest(bott))
            msg2 = await BThon4.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon4.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon4.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon5.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
	
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗕𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗕𝗧𝗛𝗢𝗡    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗗𝗮𝗥𝗞  ※

╰───⌯𝗕𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

@BThon5.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_username)
    await BThon5.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon5.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_usernamee)
    await BThon5.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon5.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_usernameee)
    await BThon5.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon5.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def _(event):
    await event.reply("**جاري تجميع النقاط**")
    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_usernameeee)
    await BThon5.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon5.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_username)
    await BThon5.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")
    
    
    
@BThon5.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_usernamee)
    await BThon5.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")

@BThon5.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_usernameee)
    await BThon5.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon5.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_usernameeee)
    await BThon5.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")


@BThon5.on(events.NewMessage(outgoing=True, pattern=".تجميع مهدويون "))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await BThon5(JoinChannelRequest('BThon'))
    channel_entity = await BThon5.get_entity(bot_usernameeeee)
    await BThon5.send_message(bot_usernameeeee, '/start')
    await asyncio.sleep(4)
    msg0 = await BThon5.get_messages(bot_usernameeeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await BThon5.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await BThon5(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await BThon5.send_message(event.chat_id, f"**تم الانتهاء من التجميع | BT**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await BThon5(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await BThon5(ImportChatInviteRequest(bott))
            msg2 = await BThon5.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await BThon5.get_messages(bot_usernameeeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await BThon5.send_message(event.chat_id, "**تم الانتهاء من التجميع | BT**")




@BThon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon1.send_message(bot_username, pt)
    sleep(4)
    msg = await BThon1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await BThon1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await BThon1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await BThon1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@BThon1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon1.on(events.NewMessage(outgoing=False, pattern=r'^/pt5 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(bot_usernameeeee, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon1.send_message(bot_usernameeeee, pt)
    sleep(4)
    msg = await BThon1.get_messages(bot_usernameeeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@BThon1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await BThon1.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await BThon1(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                



@BThon2.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon2.send_message(bot_username, pt)
    sleep(4)
    msg = await BThon2.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon2.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon2.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await BThon2.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon2.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon2.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await BThon2.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon2.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon2.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await BThon2.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon2.on(events.NewMessage(outgoing=False, pattern=r'^/pt5 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_usernameeeee, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon2.send_message(bot_usernameeeee, pt)
    sleep(4)
    msg = await BThon2.get_messages(bot_usernameeeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon2.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon2.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon2.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon2.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@BThon2.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon2.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon2.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon2.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@BThon2.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await BThon2.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await BThon2(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                



@BThon3.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon3.send_message(bot_username, pt)
    sleep(4)
    msg = await BThon3.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon3.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon3.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await BThon3.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon3.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon3.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await BThon3.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon3.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon3.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await BThon3.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon3.on(events.NewMessage(outgoing=False, pattern=r'^/pt5 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_usernameeeee, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon3.send_message(bot_usernameeeee, pt)
    sleep(4)
    msg = await BThon3.get_messages(bot_usernameeeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon3.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon3.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon3.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon3.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@BThon3.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon3.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon3.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon3.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@BThon3.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await BThon3.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await BThon3(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                



@BThon4.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon4.send_message(bot_username, pt)
    sleep(4)
    msg = await BThon4.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon4.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon4.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await BThon4.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon4.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon4.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await BThon4.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon4.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon4.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await BThon4.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon4.on(events.NewMessage(outgoing=False, pattern=r'^/pt5 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_usernameeeee, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon4.send_message(bot_usernameeeee, pt)
    sleep(4)
    msg = await BThon4.get_messages(bot_usernameeeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon4.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon4.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon4.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon4.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@BThon4.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon4.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon4.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon4.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@BThon4.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await BThon4.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await BThon4(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                



@BThon5.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon5.send_message(bot_username, pt)
    sleep(4)
    msg = await BThon5.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon5.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon5.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await BThon5.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon5.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon5.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await BThon5.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon5.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon5.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await BThon5.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@BThon5.on(events.NewMessage(outgoing=False, pattern=r'^/pt5 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_usernameeeee, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_usernameeeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await BThon5.send_message(bot_usernameeeee, pt)
    sleep(4)
    msg = await BThon5.get_messages(bot_usernameeeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon5.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon5.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon5.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon5.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@BThon5.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon5.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@BThon5.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await BThon5.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@BThon5.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await BThon5.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await BThon5(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
       

@BThon1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await BThon1.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    
@BThon2.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await BThon2.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
@BThon3.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await BThon3.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**") 

@BThon4.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await BThon4.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**") 

@BThon5.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await BThon5.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**") 


@BThon1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @EEObot - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @TTNBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`
• @MHDN313bot - `/pt5 + عدد النقاط`**""")

@BThon2.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @EEObot - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @TTNBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`
• @MHDN313bot - `/pt5 + عدد النقاط`**""")

@BThon3.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @EEObot - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @TTNBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`
• @MHDN313bot - `/pt5 + عدد النقاط`**""")


@BThon4.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @EEObot - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @TTNBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`
• @MHDN313bot - `/pt5 + عدد النقاط`**""")

@BThon5.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @EEObot - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @TTNBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`
• @MHDN313bot - `/pt5 + عدد النقاط`**""")


@BThon1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @EEObot - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @TTNBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@BThon2.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @EEObot - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @TTNBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@BThon3.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @EEObot - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @TTNBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@BThon4.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @EEObot - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @TTNBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@BThon5.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @EEObot - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @TTNBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")

@BThon1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await BThon1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@BThon1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await BThon1.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@BThon1.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await BThon1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await BThon1(JoinChannelRequest('d3boot_7'))
        joinw = await BThon1(JoinChannelRequest('Fvvvv'))
        joine = await BThon1(JoinChannelRequest('DzDDDD'))
        joinr = await BThon1(JoinChannelRequest('botbillion'))
        joint = await BThon1(JoinChannelRequest('zzzzzz1'))
        joiny = await BThon1(JoinChannelRequest('zzzzzz'))

        joini = await BThon1(JoinChannelRequest('zz_MX'))
        joino = await BThon1(JoinChannelRequest('zd_e6'))
        joinp = await BThon1(JoinChannelRequest('KTTTT'))
        joina = await BThon1(JoinChannelRequest('RRXFR'))
        sendd = await BThon1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@BThon2.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon2.send_message(userbt, '/start')
     sleep(2)
    msg1 = await BThon2.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@BThon2.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await BThon2.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@BThon2.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await BThon2.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await BThon2(JoinChannelRequest('d3boot_7'))
        joinw = await BThon2(JoinChannelRequest('Fvvvv'))
        joine = await BThon2(JoinChannelRequest('DzDDDD'))
        joinr = await BThon2(JoinChannelRequest('botbillion'))
        joint = await BThon2(JoinChannelRequest('zzzzzz1'))
        joiny = await BThon2(JoinChannelRequest('zzzzzz'))

        joini = await BThon2(JoinChannelRequest('zz_MX'))
        joino = await BThon2(JoinChannelRequest('zd_e6'))
        joinp = await BThon2(JoinChannelRequest('KTTTT'))
        joina = await BThon2(JoinChannelRequest('RRXFR'))
        sendd = await BThon2.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@BThon3.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon3.send_message(userbt, '/start')
     sleep(2)
    msg1 = await BThon3.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@BThon3.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await BThon3.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@BThon3.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await BThon3.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await BThon3(JoinChannelRequest('d3boot_7'))
        joinw = await BThon3(JoinChannelRequest('Fvvvv'))
        joine = await BThon3(JoinChannelRequest('DzDDDD'))
        joinr = await BThon3(JoinChannelRequest('botbillion'))
        joint = await BThon3(JoinChannelRequest('zzzzzz1'))
        joiny = await BThon3(JoinChannelRequest('zzzzzz'))

        joini = await BThon3(JoinChannelRequest('zz_MX'))
        joino = await BThon3(JoinChannelRequest('zd_e6'))
        joinp = await BThon3(JoinChannelRequest('KTTTT'))
        joina = await BThon3(JoinChannelRequest('RRXFR'))
        sendd = await BThon3.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@BThon4.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon4.send_message(userbt, '/start')
     sleep(2)
    msg1 = await BThon4.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@BThon4.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await BThon4.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@BThon4.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await BThon4.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await BThon4(JoinChannelRequest('d3boot_7'))
        joinw = await BThon4(JoinChannelRequest('Fvvvv'))
        joine = await BThon4(JoinChannelRequest('DzDDDD'))
        joinr = await BThon4(JoinChannelRequest('botbillion'))
        joint = await BThon4(JoinChannelRequest('zzzzzz1'))
        joiny = await BThon4(JoinChannelRequest('zzzzzz'))

        joini = await BThon4(JoinChannelRequest('zz_MX'))
        joino = await BThon4(JoinChannelRequest('zd_e6'))
        joinp = await BThon4(JoinChannelRequest('KTTTT'))
        joina = await BThon4(JoinChannelRequest('RRXFR'))
        sendd = await BThon4.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@BThon5.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await BThon5.send_message(userbt, '/start')
     sleep(2)
    msg1 = await BThon5.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
        
@BThon5.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        msg = await BThon5.get_messages(userbott, limit=1)
        await msg[0].forward_to(ownerhson_id)
        
@BThon5.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await BThon5.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await BThon5(JoinChannelRequest('d3boot_7'))
        joinw = await BThon5(JoinChannelRequest('Fvvvv'))
        joine = await BThon5(JoinChannelRequest('DzDDDD'))
        joinr = await BThon5(JoinChannelRequest('botbillion'))
        joint = await BThon5(JoinChannelRequest('zzzzzz1'))
        joiny = await BThon5(JoinChannelRequest('zzzzzz'))

        joini = await BThon5(JoinChannelRequest('zz_MX'))
        joino = await BThon5(JoinChannelRequest('zd_e6'))
        joinp = await BThon5(JoinChannelRequest('KTTTT'))
        joina = await BThon5(JoinChannelRequest('RRXFR'))
        sendd = await BThon5.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
        


print("💠 BThon Userbot Running 💠")
BThon1.run_until_disconnected()
BThon2.run_until_disconnected()
BThon3.run_until_disconnected()
BThon4.run_until_disconnected() 
BThon5.run_until_disconnected()

#code skip accumulate points by t.me.zzzzl1l thank you my bro
#The code has been updated py Dark
