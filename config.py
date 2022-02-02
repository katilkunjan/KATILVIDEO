import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "KATIL MUSIC")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGODB_URL = getenv("MONGODB_URL")
OWNER_NAME = getenv("OWNER_NAME", "༒★[•亗『𝐊𝐀𝐓𝐈𝐋』亗•]★")
ALIVE_NAME = getenv("ALIVE_NAME", "KATIL MUSIC)
BOT_USERNAME = getenv("BOT_USERNAME", "KATIL_MUSIC")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "KATIL_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "FULL_MASTI_CLUBS")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "HEARTBROKENPERSON1")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/7e1c3a6fa1ae179b7c2c4.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Katilkunjan/KATILVIDEO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/7e1c3a6fa1ae179b7c2c4.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/7e1c3a6fa1ae179b7c2c4.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/7e1c3a6fa1ae179b7c2c4.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/7e1c3a6fa1ae179b7c2c4.jpg")
