import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", "1522049"))
    API_HASH = os.environ.get("API_HASH", "c30feec37135900e0d7d6be892f694fd")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2049238855:AAFNAQ2yXezitUxrnb-q35cnNQNOHwH987M")
    START_MSG = os.environ.get("START_MSG", "<b>හායි 👋 {},\nමම EDMGANGX Music Downloader Bot 🤖,</b>\n\n /give විධානය සමඟ ඕනෑම ගීතයක නමක් මට එවන්න. (උදා - /give andakare man)")
    START_IMG = os.environ.get("START_IMG", "https://cdn.discordapp.com/attachments/852754993626218516/899683133383901244/PicsArt_10-18-09.09.11.jpg")
    OWNER = os.environ.get("OWNER", "edmgangx") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
