# Credit @
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22301731"))
    API_HASH = getenv("API_HASH", "6cc5c27041a110b47b3e804225e8ab33")
    BOT_TOKEN = getenv("BOT_TOKEN", "7618429387:AAEo7pd4lrxCXno2qpmDlkh9erM4sgCMikI")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1001805846204")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "5989980107").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Sahil:<db_password>@cluster0.njg1t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
