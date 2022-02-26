class script(object):
    START_TXT = """Hᴇʏ {},
        Mʏ ɴᴀᴍᴇ ɪs Jᴇɴɴɪᴇ.. ☺
        
        Pʟᴇᴀsᴇ ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ..😄"""
    HELP_TXT = """𝙷𝙴𝚈 {}
Tʜᴇsᴇ Aʀᴇ Tʜᴇ Aᴠᴀɪʟᴀʙʟᴇ Lɪsᴛ Oғ Mʏ Cᴏᴍᴍᴀɴᴅs."""
    ABOUT_TXT = """ 𝑯𝒆𝒚 {}, 𝑰 𝑨𝒎 𝑱𝒆𝒏𝒏𝒊𝒆
    
  ❥ 🧠 Dᴇᴠᴇʟᴏᴘᴇʀ      :  <a href=https://t.me/Username_Not_Found_404_Error>𝗔ʀᴊᴜɴ☆ IQ³⁶⁹×ˣ</a>
  
  ❥ 🎞 Lɪʙʀᴀʀʏ           : 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺
  
  ❥ 🔧 Lᴀɴɢᴜᴀɢᴇ        : 𝗣𝘆𝘁𝗵𝗼𝗻 𝟯
  
  ❥ 🏳 DᴀᴛᴀBᴀsᴇ        : 𝗠𝗼𝗻𝗴𝗼 𝗗𝗯
  
  ❥ 🚧 Hᴏsᴛᴇᴅ Oɴ     : 𝗛𝗲𝗿𝗼𝗸𝘂
    
  ❥ 🕐 Bᴜɪʟᴅ Sᴛᴀᴛᴜs :  𝗩 𝟭𝟵.𝟴"""
    
    FLTR_TXT = """Help: <b>𝗙𝗜𝗟𝗧𝗘𝗥𝗦</b>
    
    ❥ 𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝘁𝗵𝗲 𝗰𝘂𝗿𝗿𝗲𝗻𝘁𝗹𝘆 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗲 𝗳𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝗼𝗳 𝗝𝗲𝗻𝗻𝗶𝗲..
      𝗠𝗼𝗿𝗲 𝗳𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝘄𝗶𝗹𝗹 𝗯𝗲 𝘃𝗶𝘀𝗶𝗯𝗹𝗲 𝗼𝗻 𝗳𝘂𝘁𝘂𝗿𝗲."""
    IKKA_TXT = """𝐂𝐀𝐔𝐓𝐈𝐎𝐍 : <b>Iᴋᴋᴀ Fᴀɴs Aʀᴇ Pʀᴏʜɪʙɪᴛᴇᴅ Nᴇᴀʀ Tʜɪs ᴀʀᴇᴀ</b> 
    
    <b> 𝙍𝙀𝘼𝙎𝙊𝙉: </b>

    Tʜɪs ғɪʟᴛᴇʀ ᴄᴏɴᴛᴀɪɴs ᴛᴏxɪᴄ ғᴜɴɴʏ sᴛɪᴄᴋᴇʀs 😂😂😂
    
    <b> 𝘾𝙊𝙈𝙈𝘼𝙉𝘿: </b> /guhan ☺☺
    
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

<b>Cᴏᴍᴍᴀɴᴅs:</b>

𝗦𝗲𝗻𝗱 /alive 𝘁𝗼 𝗰𝗵𝗲𝗰𝗸 𝘄𝗵𝗲𝘁𝗵𝗲𝗿 𝗜 𝗮𝗺 𝗮𝗹𝗶𝘃𝗲 𝗼𝗿 𝗻𝗼𝘁...😂😂

"""
    HELPME_TXT = """Help: <b>Help 😂</b>

<b>Commands:</b>

Sᴇɴᴅ /help ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ ғʀᴏᴍ ᴍᴇ...😂😂

"""
    SOURCEJ_TXT = """<b>Source:</b>
Jennie is an Open source project.

<b>DEVS:</b>
- <a href='https://t.me/Username_Not_Found_404_Error'>Aʀᴊᴜɴ</a>
"""
    WHOIS_TXT ="""Help: <b>WHO IS - MODULE</b>
    
    Usᴀɢᴇ- Gɪᴠᴇ ᴀ ᴜsᴇʀ ᴅᴇᴛᴀɪʟs

    •/ᴡʜᴏɪs :-Gɪᴠᴇs Fᴜʟʟ Dᴇᴛᴀɪʟs Oғ Aɴ Usᴇʀ.."""
        
    NETPING_TXT = """Help: <b>Ping</b>

<b>Commands:</b>

Sᴇɴᴅ /ping ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ɪɴᴛᴇʀɴᴇᴛ sᴘᴇᴇᴅ...

"""
    GAMES_TXT ="""<b>FUN MODULE</b> 
    
<b>𝑵𝑶𝑻𝑯𝑰𝑵𝑮 𝑴𝑼𝑪𝑯, 𝑱𝑼𝑺𝑻 𝑺𝑶𝑴𝑬 𝑭𝑼𝑵 𝑮𝑨𝑴𝑬𝑺 𝑻𝑶 𝑷𝑨𝑺𝑺 𝑻𝑯𝑬 𝑻𝑰𝑴𝑬</b>"""
    
    AUNTY_TXT ="""<b>THE GREAT MALLU AUNTY</b>
   
 Sᴇɴᴅ /aunty, 
 
 Tʜᴇɴ Mᴀʟʟᴜ Aᴜɴᴛʏ Wɪʟʟ Tᴇxᴛ Yᴏᴜ Sᴏᴍᴇ Jᴏᴋᴇs 😂😂 """
        
    ARROW_TXT ="""<b>Throw / Dart</b>
    
    Sᴇɴᴅ /throw 𝗈𝗋 /dart - 𝖳𝗈 𝖬𝖺𝗄𝖾 Dʀᴀᴛ...
    
    😄😊"""
    
    DICE_TXT ="""<b>THE DICE..</b>
    
    Sᴇɴᴅ /dice Tᴏ Rᴏʟʟ A Dɪᴄᴇ...
    
    😄😊"""
    
    GOAL_TXT ="""<b>THE DICE..</b>
    
    Sᴇɴᴅ /goal ᴏʀ /shoot - Tᴏ Mᴀᴋᴇ A Gᴏᴀʟ Oʀ Sʜᴏᴏᴛ...
    
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

<b>Aʟʟ Tʜᴇ Pɪɴ Rᴇʟᴀᴛᴇᴅ Cᴏᴍᴍᴀɴᴅs Cᴀɴ Bᴇ Fᴏᴜɴᴅ Hᴇʀᴇ; Kᴇᴇᴘ Yᴏᴜʀ Cʜᴀᴛ Uᴘ Tᴏ Dᴀᴛᴇ Oɴ Tʜᴇ Lᴀᴛᴇsᴛ Nᴇᴡs Wɪᴛʜ A Sɪᴍᴘʟᴇ Pɪɴɴᴇᴅ Mᴇssᴀɢᴇ!</b>

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>

◉ /Pɪɴ :- Pɪɴ Tʜᴇ Mᴇssᴀɢᴇ Yᴏᴜ Rᴇᴘʟɪᴇᴅ Tᴏ Mᴇssᴀɢᴇ Tᴏ Sᴇɴᴅ A Nᴏᴛɪғɪᴄᴀᴛɪᴏɴ Tᴏ Gʀᴏᴜᴘ Mᴇᴍʙᴇʀs..

◉ /Uɴᴘɪɴ :- Uɴᴘɪɴ Tʜᴇ Cᴜʀʀᴇɴᴛ Pɪɴɴᴇᴅ Mᴇssᴀɢᴇ. Iғ Usᴇᴅ As A Rᴇᴘʟʏ, Uɴᴘɪɴs Tʜᴇ Rᴇᴘʟɪᴇᴅ Tᴏ Mᴇssᴀɢᴇ"""
    PURGE_TXT = """Help: <b>Purge</b>
Nᴇᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʟᴏᴛs ᴏғ ᴍᴇssᴀɢᴇs? Tʜᴀᴛ's ᴡʜᴀᴛ ᴘᴜʀɢᴇs ᴀʀᴇ ғᴏʀ!

<b>Commands and Usage:</b>

• /ᴘᴜʀɢᴇ - ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇ, ᴛᴏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴍᴇssᴀɢᴇ.

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ Oɴʟʏ ᴀᴅᴍɪɴ."""
    BREAKUP_TXT = """HELP: <b>Break Up</b>
    
    Sᴇɴᴅ ᴍᴇ /breakup..🥺🥺
    
    """
    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>
    
- Send me /password command.. to make a password😄.

- I Will Give The Password...

<b>Commands and Usage:</b>

• /password

"""
    TGRAPH_TXT = """Help: <b>Tᴇʟᴇɢʀᴀᴘʜ</b>
    
Dᴏ ᴀs ʏᴏᴜ ᴡɪsʜ ᴡɪᴛʜ ᴛᴇʟᴇɢʀᴀᴘʜ ᴍᴏᴅᴜʟᴇ!

<b>Commands and Usage:</b>

• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄
 Yᴏᴜ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴀ PDF ғɪʟᴇ ᴛᴏ ᴀɴ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ 

 Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:
 
 /audiobook: Rᴇᴘʟʏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀɴʏ PDF ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴛʜᴇ ᴀᴜᴅɪᴏ"""

    INFO_TXT = """Help: <b>Information</b>
    
Gᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ sᴏᴍᴇᴛʜɪɴɢ!

<b>Commands and Usage:</b>

• /id - get id of a specified user.
• /info  - get information about a user.

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    JSON_TXT = """Help: <b>Json</b>
Gᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏғ ᴀ ᴍᴇssᴀɢᴇ!

<b>Commands and Usage:</b>

• /json - get the json details of a message.

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    TTS_TXT = """Help: <b>Text to Speech</b>
    
A ᴍᴏᴅᴜʟᴇ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ᴛᴏ ᴠᴏɪᴄᴇ ᴡɪᴛʜ ʟᴀɴɢᴜᴀɢᴇ sᴜᴘᴘᴏʀᴛ.

<b>Commands and Usage:</b>

• /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    CORONA_TXT ="""<b>Hᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴛʜᴇ ᴄᴏʀᴏɴ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴍᴏᴅᴜʟᴇ</b>
    
➡️ /covid <code>(countryname)</code> <b>ʏᴏᴜ ᴄᴀɴ ғɪɴᴅ ᴀ ᴄᴏʀᴏɴᴀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴏғ ᴀɴʏ ᴄᴏᴜɴᴛʀʏ</b>

➡️ <b>example</b> : - /covid India"""
    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>
    
A ᴍᴏᴅᴜʟᴇ ᴛʜᴀᴛ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ sʜᴏʀᴛᴇɴ ᴜʀʟs

<b>Commands and Usage:</b>

• /short <code>(link)</code> - I will send the shorted links.
<b>Example:</b>
<code>/short https://t.me/tomoviesall</code>

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    SHARE_TXT = """Help: <b>Sharing Text Maker</b>

A feature to create a link to share text in the telegram.

<b>Commands and Usage:</b>
• /share (text or reply to message)

<b>NOTE:</b>
• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    MUSIC_TXT = """Help: <b>YT Music Downloader</b>
    
Mᴜsɪᴄ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇs, ғᴏʀ ᴛʜᴏsᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜsɪᴄ.

<b>Commands and Usage:</b>

• /song or /mp3 (songname) - ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴛ sᴇʀᴠᴇʀs.

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    MP4_TXT = """Help: <b>YT Video Downloader</b>
    
    Vɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇs, ғᴏʀ ᴛʜᴏsᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴠɪᴅᴇᴏs.
    
• /video or /mp4 (videoname) - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴛ sᴇʀᴠᴇʀs.

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    THUMBNAIL_TXT = """Help: <b>Thumbnail Downloader</b>
    
    Tʜᴜᴍʙɴᴀɪʟ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇs, ғᴏʀ ᴛʜᴏsᴇ ᴡʜᴏ ʟᴏᴠᴇ Tʜᴜᴍʙɴᴀɪʟs.
    
<b>YouTube Thumbnail Download</b>

• /ytthumb (youtube link)

<b>Example:</b> <code>/ytthumb https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=22s</code>

<b>NOTE:</b>

• Bᴏᴛ sʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡᴏʀᴋs ᴏɴ ʙᴏᴛʜ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ʙʏ ᴀɴʏ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ."""
    DEAD_TXT = """Help: <b>Zombies</b>
    
<b>Kɪᴄᴋ ɪɴᴄᴀᴛɪᴠᴇ ᴍᴇᴍʙᴇʀs ғʀᴏᴍ ɢʀᴏᴜᴘ. Aᴅᴅ ᴍᴇ ᴀs ᴀᴅᴍɪɴ ᴡɪᴛʜ ʙᴀɴ ᴜsᴇʀs ᴘᴇʀᴍɪssɪᴏɴ ɪɴ ɢʀᴏᴜᴘ.</b>

<b>Commands and Usage:</b>

• /inkick - command with required arguments and i will kick members from group.

• /instatus - to check current status of chat member from group.

• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.

• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.

• /dkick - to kick deleted accounts."""
    
    STICKER_TXT ="""<b>Sᴇɴᴅ /stickerid As ᴛʜᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ sᴛɪᴄᴋᴇʀ ᴛᴏ ғɪɴᴅ ɪᴛs ID</b>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Jᴇɴɴɪᴇ Sᴜᴘᴘᴏʀᴛs ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs.

<b>NOTE:</b>

1. Tᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
2. Jᴇɴɴɪᴇ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
3. Bᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+WqhO2sfnZxcxYjk1)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>

"""
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

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /id - ɢᴇᴛ ɪᴅ ᴏғ ᴀ sᴘᴇᴄɪғɪᴇᴅ ᴜsᴇʀ.
• /info  - ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜsᴇʀ.
• /imbd - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ IMDʙ sᴏᴜʀᴄᴇ.
• /search  - ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜs sᴏᴜʀᴄᴇs."""
    ADMIN_TXT = """Help: <b>Aᴅᴍɪɴ Mᴏᴅᴜʟᴇs</b>

<b>NOTE:</b>
Tʜɪs ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋs ғᴏʀ ᴍʏ ᴀᴅᴍɪɴs

<b>Cᴏᴍᴍᴀɴᴅs ᴀɴᴅ Usᴀɢᴇ:</b>
• /logs - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇsᴄᴇɴᴛ ᴇʀʀᴏʀs.

• /stats - ᴛᴏ ɢᴇᴛ sᴛᴀᴛᴜs ᴏғ ғɪʟᴇs ɪɴ ᴅʙ.

• /delete - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ sᴘᴇᴄɪғɪᴄ ғɪʟᴇ ғʀᴏᴍ ᴅʙ.

• /users - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴍʏ ᴜsᴇʀs ᴀɴᴅ ɪᴅs.

• /chats - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛs ᴀɴᴅ ɪᴅs.

• /leave  - ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.

• /disable  -  ᴅᴏ ᴅɪsᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.

• /ban  - ᴛᴏ ʙᴀɴ ᴀ ᴜsᴇʀ.

• /unban  - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ.

• /channel - ᴛᴏ ɢᴇᴛ ʟɪsᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟs.

• /broadcast - ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜsᴇʀs"""
    STATUS_TXT = """
 🧲  Iɴᴅᴇxᴇᴅ Fɪʟᴇs  :     <code>{}</code>
    
 👨‍👨‍👦‍👦 Hᴀɴᴅʟɪɴɢ Usᴇʀs : <code>{}</code>
 
 🎟  Aᴅᴅᴇᴅ Cʜᴀᴛs  :      <code>{}</code>
 
 🏛  Sᴛᴏʀᴀɢᴇ Usᴇᴅ :     <code>{}</code> ᴍɪʙ
 
 🕋 Cᴀᴘᴀᴄɪᴛʏ : <code>{}</code> ᴍɪʙ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
