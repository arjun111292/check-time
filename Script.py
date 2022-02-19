class script(object):
    START_TXT = """Hᴇʏ {},
        Mʏ ɴᴀᴍᴇ ɪs Jᴇɴɴɪᴇ `BLΛƆKPIИK,Pʟᴇᴀsᴇ ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ.."""
    HELP_TXT = """𝙷𝙴𝚈 {}
Tʜᴇsᴇ Aʀᴇ Tʜᴇ Aᴠᴀɪʟᴀʙʟᴇ Lɪsᴛ Oғ Mʏ Cᴏᴍᴍᴀɴᴅs."""
    ABOUT_TXT = """ 𝑯𝒆𝒚, 𝑰 𝑨𝒎 𝑱𝒆𝒏𝒏𝒊𝒆
  ❥ Cʀᴇᴀᴛᴏʀ:  <a href=@Arjun_La_Lis_A>𝗔𝗿𝗷𝘂𝗻</a>
  ❥ Lɪʙʀᴀʀʏ:     𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺
  ❥ Lᴀɴɢᴜᴀɢᴇ:    𝗣𝘆𝘁𝗵𝗼𝗻 𝟯
  ❥ Dᴀᴛᴀ Bᴀsᴇ:   𝗠𝗼𝗻𝗴𝗼 𝗗𝗕
  ❥ Bᴏᴛ Sᴇʀᴠᴇʀ:  𝗛𝗲𝗿𝗼𝗸𝘂"""
    FLTR_TXT = """Help: <b>Filters</b>
    
    These are the currently availabe features of Jennie,More features will be visible on future."""
    IKKA_TXT = """CAUTION : <b> Ikka Fans Are Prohibited Near This area </b> 
    
    <b> REASON: </b>

    This filter contains toxic funny stickers 😂😂😂
    
    """
    
    MANUELFILTER_TXT = """Help: <b>Mᴀɴᴜᴀʟ Fɪʟᴛᴇʀ</b>

- Fɪʟᴛᴇʀ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜsᴇʀs ᴄᴀɴ sᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇs ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ Jᴇɴɴɪᴇ ᴡɪʟʟ ʀᴇsᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪs ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ
<b>NOTE:</b>
          
1. Jᴇɴɴɪᴇ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴs ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 64 ᴄʜᴀʀᴀᴄᴛᴇʀs.

<b>Commands and Usage:</b>
• /filter - ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ
• /filters - ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀs ᴏғ ᴀ ᴄʜᴀᴛ
• /del - ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ
• /delall - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ (chat owner only)"""

    AUTOFILTER_TXT = """Help: <b>Aᴜᴛᴏᴍᴀᴛɪᴄ Fɪʟᴛᴇʀ</b>

<b>NOTE:</b>
1. Mᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
2. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇs.
3. Fᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.
 I'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ."""
    ALIVE_TXT = """Help: <b>Alive</b>

<b>Commands:</b>

Send /alive to check whether I am alive or not...😂😂

"""
    HELPME_TXT = """Help: <b>Help 😂</b>

<b>Commands:</b>

Send /help if you need any help from me...😂😂

"""
    SOURCEJ_TXT = """<b>Source:</b>
Jennie is a Open source project.

<b>DEVS:</b>
- <a href='https://t.me/Arjun_La_Lis_A'>Aʀᴊᴜɴ</a>
"""
    WHOIS_TXT ="""Help: <b>WHO IS MODULE</b>
    
    Usage- Give a user details

    •/whois :-Gives Full Details Of An User.."""
        
    NETPING_TXT = """Help: <b>Ping</b>

<b>Commands:</b>

Send /ping to check your internet speed...

"""
    GAMES_TXT ="""<b>FUN MODULE</b> 
    
<b>NOTHING MUCH, JUST SOME FUN GAMES TO PASS THE TIME</b>"""
    
    AUNTY_TXT ="""<b>THE GREAT MALLU AUNTY</b>
    
    Send /aunty Then Mallu Aunty Will Text You Some Jokes 😂😂 """
        
    ARROW_TXT ="""<b>Throw / Dart</b>
    
    Send /throw 𝗈𝗋 /dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Drat... 
    
    😄😊"""
    
    DICE_TXT ="""<b>THE DICE..</b>
    
    Send /dice To Roll A Dice... 
    
    😄😊"""
    
    GOAL_TXT ="""<b>THE DICE..</b>
    
    Send /goal or /shoot - To Make A Goal Or Shoot...
    
    😄😊"""
    
    GTRANS_TXT = """Help: <b>Tʀᴀɴsʟᴀᴛᴏʀ</b>
Tʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛs ᴛᴏ ᴀ sᴘᴇᴄɪғɪᴄ ʟᴀɴɢᴜᴀɢᴇ!
<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /tr [language code][reply] - ᴛʀᴀɴsʟᴀᴛᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ᴛᴏ sᴘᴇᴄɪғɪᴄ ʟᴀɴɢᴜᴀɢᴇ.
<b>NOTE:</b>
• Jᴇɴɴɪᴇ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Rᴇᴘʟʏ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛᴇxᴛ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Jᴇɴɴɪᴇ ᴄᴀɴ ᴛʀᴀɴsʟᴀᴛᴇ ᴛᴇxᴛs ᴛᴏ 200+ ʟᴀɴɢᴜᴀɢᴇs."""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin :</b>
<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>
<b>Commands and Usage:</b>
◉ /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members..
◉ /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    PURGE_TXT = """Help: <b>Purge</b>
Need to delete lots of messages? That's what purges are for!
<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""
    BREAKUP_TXT = """HELP: <b>Break Up</b>
    
    Send me /breakup..🥺🥺
    
    """
    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>
    
- Send me /password command.. to make a password😄.

- I Will Give The Password...

<b>Commands and Usage:</b>
• /password

"""
    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>
Do as you wish with telegra.ph module!
<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚘𝚗𝚟𝚎𝚛𝚝 𝚊 𝙿𝙳𝙵 𝚏𝚒𝚕𝚎 𝚝𝚘 𝚊 𝚊𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚝𝚑 𝚝𝚑𝚒𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 ✯
➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:
➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    INFO_TXT = """Help: <b>Information</b>
Get information about something!
<b>Commands and Usage:</b>
• /id - get id of a specified user.
• /info  - get information about a user.
• /json - get the json details of a message.
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    JSON_TXT = """Help: <b>Json</b>
Get information of a message!
<b>Commands and Usage:</b>
• /json - get the json details of a message.
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    TTS_TXT = """Help: <b>Text to Speech</b>
A module to convert text to voice with language support.
<b>Commands and Usage:</b>
• /tts - Reply to any text message with language code to convert as audio.
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
➡️ /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>
➡️ <b>example</b> : - /covid India"""
    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>
Some URLs is Shortner
<b>Commands and Usage:</b>
• /short <code>(link)</code> - I will send the shorted links.
<b>Example:</b>
<code>/short https://t.me/tomoviesall</code>
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

A feature to create a link to share text in the telegram.

<b>Commands and Usage:</b>
• /share (text or reply to message)

<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    MUSIC_TXT = """Help: <b>YT Music Downloader</b>
Music download modules, for those who love music.
<b>Commands and Usage:</b>
• /song or /mp3 (songname) - download song from yt servers.
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    MP4_TXT = """Help: <b>YT Video Downloader</b>
    Video download modules, for those who love videos.
• /video or /mp4 (videoname) - download video from yt servers.
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    THUMBNAIL_TXT = """Help: <b>Thumbnail Downloader</b>
    Thumbnail download modules, for those who love Thumbnails.
<b>YouTube Thumbnail Download</b>
• /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=22s</code>
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    DEAD_TXT = """Help: <b>Zombies</b>
<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>
<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""
    STICKER_TXT ="""<b>Send /stickerid As the reply to a sticker to find its ID</b>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Jᴇɴɴɪᴇ Sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>NOTE:</b>
1. Tᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. Jᴇɴɴɪᴇ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. Bᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+WqhO2sfnZxcxYjk1)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    CONNECTION_TXT = """Help: <b>Aᴛᴛᴀᴄʜᴍᴇɴᴛs</b>

- Usᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ PM ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀs 
- ɪᴛ ʜᴇʟᴘs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘs.

<b>NOTE:</b>
1. Oɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
2. Sᴇɴᴅ <code>/ᴄᴏɴɴᴇᴄᴛ</code> ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ PM

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /ᴄᴏɴɴᴇᴄᴛ  - ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ PM
• /ᴅɪsᴄᴏɴɴᴇᴄᴛ  - ᴅɪsᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ
• /ᴄᴏɴɴᴇᴄᴛɪᴏɴs - ʟɪsᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴs"""
    EXTRAMOD_TXT = """Help: <b>Cᴜsᴛᴏᴍ Mᴏᴅᴜʟᴇs</b>

<b>NOTE:</b>
ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs ᴏғ Jᴇɴɴɪᴇ

<ʙ>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</ʙ>
• /ɪᴅ - ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.
• /ɪɴғᴏ  - ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.
• /ɪᴍᴅʙ  - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ IMDʙ sᴏᴜʀᴄᴇ.
• /sᴇᴀʀᴄʜ  - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇs."""
    ADMIN_TXT = """Help: <b>Aᴅᴍɪɴ Mᴏᴅᴜʟᴇs</b>

<b>NOTE:</b>
Tʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴs

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /ʟᴏɢs - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇsᴄᴇɴᴛ ᴇʀʀᴏʀs</ᴄᴏᴅᴇ>
• /sᴛᴀᴛs - ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ ғɪʟᴇs ɪɴ ᴅʙ.</ᴄᴏᴅᴇ>
• /ᴅᴇʟᴇᴛᴇ - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴇ ғʀᴏᴍ ᴅʙ.</ᴄᴏᴅᴇ>
• /ᴜsᴇʀs - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴜsᴇʀs ᴀɴᴅ ɪᴅs.</ᴄᴏᴅᴇ>
• /ᴄʜᴀᴛs - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛs ᴀɴᴅ ɪᴅs </ᴄᴏᴅᴇ>
• /ʟᴇᴀᴠᴇ  - ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.</ᴄᴏᴅᴇ>
• /ᴅɪsᴀʙʟᴇ  -  ᴅᴏ ᴅɪsᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</ᴄᴏᴅᴇ>
• /ʙᴀɴ  - ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀ.</ᴄᴏᴅᴇ>
• /ᴜɴʙᴀɴ  - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ.</ᴄᴏᴅᴇ>
• /ᴄʜᴀɴɴᴇʟ - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟs</ᴄᴏᴅᴇ>
• /ʙʀᴏᴀᴅᴄᴀsᴛ - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs</ᴄᴏᴅᴇ>"""
    STATUS_TXT = """❊ 𝗧𝗼𝘁𝗮𝗹 𝗜𝗻𝗱𝗲𝘅𝗲𝗱 𝗙𝗶𝗹𝗲𝘀: <code>{}</code>
❊ 𝗧𝗼𝘁𝗮𝗹 𝗨𝘀𝗲𝗿𝘀: <code>{}</code>
❊ 𝗧𝗼𝘁𝗮𝗹 Chats: <code>{}</code>
❊ 𝗦𝘁𝗼𝗿𝗮𝗴𝗲 𝗨𝘀𝗲𝗱: <code>{}</code> 𝙼𝚒𝙱
❊ 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗽𝗰: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
