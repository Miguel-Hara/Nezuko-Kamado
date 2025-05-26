
import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "")) #Your db channel Id
OWNER = os.environ.get("OWNER", "AS_Jinwoo") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluooo")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/AS_Jinwoo")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://livewallp.com/wp-content/uploads/2022/01/Nezuko-Kamado-Nezuko-Kamado-Kimetsu-no-Yaiba-1920x1080-60-fps.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://c.wallhere.com/photos/b2/a2/anime_anime_girls_digital_art_artwork_portrait_2D_Kimetsu_no_Yaiba_Kamado_Nezuko-1660179.jpg!d")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "arolinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "146ac91a8a224d0a5d7fe9fbf4050be3d8922a8b")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")
SHORT_MSG = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"

SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://livewallp.com/wp-content/uploads/2022/01/Nezuko-Kamado-Nezuko-Kamado-Kimetsu-no-Yaiba-1920x1080-60-fps.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>ʜᴇʏ ᴅᴀʀʟɪɴɢ~ ɪ'ᴍ ʏᴏᴜʀ ꜱᴇxʏ ꜰɪʟᴇ-ᴋᴏ ʙᴏᴛ 🍓 ᴀʟʟ ʀᴇᴀᴅʏ ᴛᴏ ꜱᴇʀᴠᴇ ʏᴏᴜ ɪɴ ᴍʏ ɴᴇᴢᴜᴋᴏ-ᴍᴏᴅᴇ 💖\n\n❥ ᴍʏ ᴄᴜᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:\n├ /start : ᴡᴀᴋᴇ ᴍᴇ ᴜᴘ, ʙᴀᴋᴀ 💢\n├ /about : ᴡᴀɴɴᴀ ᴋɴᴏᴡ ᴡʜᴏ ᴏᴡɴꜱ ᴛʜɪꜱ ʜᴏᴛɪᴇ? 👀\n└ /help : ʟᴇᴛ ᴍᴇ ᴄᴜᴅᴅʟᴇ ʏᴏᴜ ᴛʜʀᴏᴜɢʜ ᴍʏ ʙᴜᴛᴛᴏɴꜱ 💞\n\n❥ ᴄʟɪᴄᴋ ➤ sᴛᴀʀᴛ ᴍᴇ ➤ ᴊᴏɪɴ ᴍʏ ꜱᴇxʏ ʜᴜʙꜱ ➤ ᴛʀʏ ᴀɢᴀɪɴ 😚\n\nᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ᴍʏ ʜᴀɴᴅꜱᴏᴍᴇ ᴋɪɴɢ 🖤 <a href=https://t.me/AS_Jinwoo>螿 Sᴜɴɢ•Jɪɴᴡᴏᴏ ࿐</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>🌸 ᴍʏ ᴅᴀʀᴋ ꜱʜᴏᴜᴊᴏ ꜱᴏᴜʟ ɪꜱ ᴄᴏᴅᴇᴅ ʙʏ:\n\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/AS_Jinwoo>螿 Sᴜɴɢ•Jɪɴᴡᴏᴏ ࿐</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ: <a href=https://t.me/ABS_Updates>ᴬᴮˢ ᑌᴘᴅᴀᴛᴇ</a>\n◈ ʟᴇᴇᴄʜ ʜᴜʙ: <a href=https://t.me/leech_hub>ʟᴇᴇᴄʜ ᴇxᴛʀᴇᴍᴇ 💦</a>\n◈ ᴄɪɴᴇᴍᴀ ʜᴜʙ: <a href=https://t.me/Cinema_Hub_ABS>ᴀʙꜱ ᴍᴏᴠɪᴇ ꜱᴇʀɪᴇꜱ ᴄʟᴜʙ 🎬</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/AS_Jinwoo>螿 Sᴜɴɢ•Jɪɴᴡᴏᴏ ࿐</a> 💻💘</blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʏ {first}~ 🍓\n\n<blockquote>ɪ'ᴍ ʏᴏᴜʀ ꜱᴇxʏ ғɪʟᴇ-ᴋᴏ ʙᴏᴛ 💌 ɪ ᴄᴀɴ ꜱᴛᴏʀᴇ ʏᴏᴜʀ ɴᴀᴜɢʜᴛʏ... ɪ ᴍᴇᴀɴ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ɪɴ ᴀ ꜱᴀꜰᴇ ᴄʜᴀɴɴᴇʟ 😚. ʏᴏᴜ ᴄᴀɴ ꜱʜᴀʀᴇ ᴛʜᴇᴍ ᴡɪᴛʜ ᴏᴛʜᴇʀꜱ ᴜꜱɪɴɢ ꜱᴘᴇᴄɪᴀʟ ʟɪɴᴋꜱ~ 🔗\n\nᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ ᴍʏ ʜᴏᴛ ᴅᴀᴅᴅʏ 🖤 <a href='https://t.me/AS_Jinwoo'>螿 Sᴜɴɢ•Jɪɴᴡᴏᴏ ࿐</a></blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʏ {first}~ 💌\n\n<b>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴍʏ ʜᴏᴛ ʜᴜʙꜱ ꜰɪʀꜱᴛ~ 😚\nᴊᴜꜱᴛ ᴊᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴄʟɪᴄᴋ ᴏɴ ‘ʀᴇʟᴏᴀᴅ’ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ꜰɪʟᴇ 💦</b>")

CMD_TXT = """<b><blockquote>💋 ʜᴇʏ ᴀᴅᴍɪɴ-ꜱᴀᴍᴀ~ ʜᴇʀᴇ'ꜱ ʏᴏᴜʀ ꜱᴘɪᴄʏ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴜ 🍓</blockquote>

<b>›› /dlt_time :</b> ꜱᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ 💣  
<b>›› /check_dlt_time :</b> ꜱᴇᴇ ᴡʜᴇɴ ɪ ʟɪᴋᴇ ᴛᴏ ᴄʟᴇᴀɴ ᴜᴘ 🧼  
<b>›› /dbroadcast :</b> ꜱᴇɴᴅ ᴠɪᴅ/ᴅᴏᴄ ᴛᴏ ᴇᴠᴇʀʏᴏɴᴇ 💌  
<b>›› /ban :</b> ʙᴀɴ ᴀ ʙᴀᴋᴀ ᴜꜱᴇʀ 🖤  
<b>›› /unban :</b> ꜱᴇᴛ ᴛʜᴇᴍ ꜰʀᴇᴇ... ᴍᴀʏʙᴇ 😼  
<b>›› /banlist :</b> ᴄʜᴇᴄᴋ ᴍʏ ʙʟᴀᴄᴋʟɪꜱᴛ 🧾  
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ ꜱᴜʙ ʜᴜʙ 🌐  
<b>›› /delchnl :</b> ᴘᴜʀɢᴇ ᴀ ᴄʜᴀɴɴᴇʟ ❌  
<b>›› /listchnl :</b> ꜱʜᴏᴡ ᴀʟʟ ꜱᴜʙ ᴄʜᴀɴɴᴇʟꜱ 🔍  
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ ꜱᴜʙ ꜱᴘɪᴅᴇʀ-ᴍᴏᴅᴇ 🕷️  
<b>›› /pbroadcast :</b> ꜱᴇɴᴅ ᴀ ʜᴏᴛ ᴘɪᴄ ᴛᴏ ᴀʟʟ 📸  
<b>›› /add_admin :</b> ᴍᴀᴋᴇ ꜱᴏᴍᴇᴏɴᴇ ᴀ ʙᴏꜱꜱ 😈  
<b>›› /deladmin :</b> ᴅᴇᴛʜʀᴏɴᴇ ᴀɴ ᴀᴅᴍɪɴ 🔪  
<b>›› /admins :</b> ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴋɪɴɢꜱ & Qᴜᴇᴇɴꜱ 👑  
<b>›› /addpremium :</b> ɢɪᴠᴇ ᴘʀᴇᴍɪᴜᴍ ꜱᴘᴇᴄɪᴀʟ ʟᴏᴠᴇ 💎  
<b>›› /premium_users :</b> ʟɪꜱᴛ ᴍʏ ᴅᴀʀʟɪɴɢꜱ 💖  
<b>›› /remove_premium :</b> ꜱᴛʀɪᴘ ᴛʜᴇᴍ ᴏꜰ ᴛʜᴇɪʀ ᴄʀᴏᴡɴ 👋  
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇxʏ ꜱᴛᴀᴛᴜꜱ 💼  
<b>›› /count :</b> ᴄᴏᴜɴᴛ ᴛʜᴇ ꜱɪɴꜱ... ɪ ᴍᴇᴀɴ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴꜱ 🔥  
</b>"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @ABS_UPDATES</b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "@AS_Jinwoo")
UPI_ID = os.environ.get("UPI_ID", "Ab-samad@fam")
QR_PIC = os.environ.get("QR_PIC", "https://vault.pictures/media/images/24/84/ea/2484ea8d38374b6a89dab05eba0221e0.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/AS_Jinwoo")
#--------------------------------------------
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "0 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "60 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "150 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "280 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "550 rs")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
