import os

class Development:
    LOGGER = True

    # REQUIRED
    API_ID = int(os.environ.get("API_ID", "123456"))
    API_HASH = os.environ.get("API_HASH", "your_api_hash")

    TOKEN = os.environ.get("API_KEY", "")

    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")

    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "")

    JOIN_LOGGER = int(os.environ.get("JOIN_LOGGER", "0"))
    EVENT_LOGS = int(os.environ.get("EVENT_LOGS", "0"))

    ALLOW_CHATS = True

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "")
    DB_NAME = os.environ.get("DB_NAME", "mydb")

    # LOAD CONTROL
    LOAD = []
    NO_LOAD = []

    # WEB SETTINGS
    WEBHOOK = False
    URL = None
    CERT_PATH = None
    PORT = int(os.environ.get("PORT", 5000))

    # USERS
    SUDO_USERS = []
    DEV_USERS = []
    SUPPORT_USERS = []
    WHITELIST_USERS = []

    # SPAMWATCH
    SPAMWATCH_API = ""
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL APIS
    WEATHER_API = ""
    WALL_API = ""
    AI_API_KEY = ""
    CASH_API_KEY = ""
    TIME_API_KEY = ""

    # OTHER SETTINGS
    INFOPIC = False
    STRICT_GBAN = False
    WORKERS = 4
    BAN_STICKER = ""
    ALLOW_EXCL = True

    BL_CHATS = []
    SPAMMERS = None

    DONATION_LINK = None
    DEL_CMDS = True

    BACKUP_PASS = "12345"
    DROP_UPDATES = False
