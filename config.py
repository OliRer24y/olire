## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBQWDkr3dX64vA1E4N0MNu-K69kelMI8F5wETbYhN2mdFZGtKGM5id8_8mC5qB143zFT05JQeCbPP_llT4xb7WPKbp5RqN7RRE2qcKq0QmHmBQsemEHXsoEOGCkuVJWrtujObAo7LJe_dCQybPY6L0zR61tQwcF-_ulWTn_CXyyfrxYjaJ7XQnJhFHaJ3vuspNsHTARQiMSmitaAFYTuH8q8vUXSB3eAPPneF9CGEtUUrXJa-TU-fsLJTjEbViOAajpwSMqUClM7ss-yMVT_ybiqHi83LniyE3DrJnzsa45Pk8T0F1tpoC58Je2ALVKMt-A7ILl58Q8qrpDr05b8qPTcNDUgAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5438257413:AAHfsVM7zPzRDjA0VgWrq1mDK133W40N7wI")
BOT_NAME = getenv("BOT_NAME", "𝚖𝚞𝚜𝚒𝚌 𝚋𝚘𝚝 ⁦.")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZZZZ8lZ")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "G_30_bot")
OWNER_ID = getenv("OWNER_ID", "1892734080")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Se_fm")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xl444")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZZZZ8lZ")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
