

from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22207976"))
    API_HASH = getenv("API_HASH", "5c0ad7c48a86afac87630ba28b42560d")
    BOT_TOKEN = getenv("BOT_TOKEN", "7200841820:AAFgKy1xg8EYeIMyvcibSmf7g1vinhW1VNQ")
    SUDO = list(map(int, getenv("SUDO", "6872968794")))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Autofilterbot:Autofilterbot@cluster0.1oipdqu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

