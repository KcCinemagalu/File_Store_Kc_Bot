import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "14350423"))
  API_HASH = os.environ.get("API_HASH", "838b0b81758d276215b3647821b707ad")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6490976569:AAFG9Ix44H5yXiTnNdL-BRSBceKMt_X7flc")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Godslayerfilestore_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002007676603"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "instantlinks.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "2a8d82ec088d8c8e24c9b905d1bbe305097d8d43")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6606973036"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://deendayaldhaked9:6PFNcPY4ckT7FFQp@cluster0.z536xun.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001786865459")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001990529377"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Godslayer Boruto](https://telegram.me/opabhi0)
 
 I am Super noob Please Support My Hard Work.
 #force sub channel id, if you want enable force sub

[Donate Me](https://t.me/opabhi0)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
