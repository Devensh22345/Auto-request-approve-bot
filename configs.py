# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22207976"))
    API_HASH = getenv("API_HASH", "5c0ad7c48a86afac87630ba28b42560d")
    BOT_TOKEN = getenv("BOT_TOKEN", "7365852964:AAFsKlal2wRxWjZPxYQ4sOPaz7KJyqJaIWQ")
    FSUB = getenv("FSUB", "Dk_anime_Group")
    CHID = int(getenv("CHID", "-1002204196114"))
    SUDO = list(map(int, getenv("SUDO", "6872968794").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Autofilterbot:Autofilterbot@cluster0.1oipdqu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
