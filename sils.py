import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Veez Music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/8628c642a266a22effd8c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/4c39fbb88932761913fff.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/73e10ed6e2bd32b478de6.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("@CT_NE_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "veezassistant1")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
BROADCAST_AS_COPY = ("11")
GROUP_SUPPORT = ("22")
UPDATES_CHANNEL = ("33")
LOG_CHANNEL = ("77")
