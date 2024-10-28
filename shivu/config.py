class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7038202445"
    sudo_users = "7757912959", "7038202445"
    GROUP_ID = -1002324830715
    TOKEN = "8192992847:AAErDbqs_BogqvN_vfgOKqj96jaS534yqbY"
    mongo_url = "mongodb+srv://vjimmy276:<db_password>@ztx.pxamg.mongodb.net/?retryWrites=true&w=majority&appName=ZTX"
    PHOTO_URL = ["https://graph.org/file/34ce254537a31ca2a788b-f8b59bff546af8dc58.jpg", "https://graph.org/file/0cd48cfd409203a00da74-2a919fe99dd1b238ec.jpg"]
    SUPPORT_CHAT = "https://t.me/Anime_Group_India_Chat"
    UPDATE_CHAT = "https://t.me/Shorekeeper_updates"
    BOT_USERNAME = "HosinoXharembot"
    CHARA_CHANNEL_ID = "-1002324830715"
    api_id = 23028479
    api_hash = "c1e6a93b04c0810a5c282d8d8d44ea6f"
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
