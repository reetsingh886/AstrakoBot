import os

class Development:
    LOGGER = True

    # REQUIRED
    API_ID = int(os.environ.get("API_ID", "123456"))
    API_HASH = os.environ.get("API_HASH", "your_api_hash")

    TOKEN = os.environ.get("API_KEY", "")  # Bot token

    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")

    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "")

    JOIN_LOGGER = int(os.environ.get("JOIN_LOGGER", "0"))
    EVENT_LOGS = int(os.environ.get("EVENT_LOGS", "0"))

    ALLOW_CHATS = True

    # DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "")
    DB_NAME = os.environ.get("DB_NAME", "mydb")

    # SAFE DEFAULTS (no error)
    LOAD = []
    NO_LOAD = []

    WEBHOOK = False
    URL = None
    CERT_PATH = None
    PORT = int(os.environ.get("PORT", 5000))

    # USERS
    SUDO_USERS = []
    DEV_USERS = []
    SUPPORT_USERS = []
    WHITELIST_USERS = []

    # OPTIONAL SAFE
    INFOPIC = False
    SPAMWATCH_API = ""
    WEATHER_API = ""
    WALL_API = ""
    AI_API_KEY = ""

    STRICT_GBAN = False
    WORKERS = 4
    BAN_STICKER = ""
    ALLOW_EXCL = True

    CASH_API_KEY = ""
    TIME_API_KEY = ""

    BL_CHATS = []
    SPAMMERS = None

    DONATION_LINK = None
    DEL_CMDS = True

    BACKUP_PASS = "12345"
    DROP_UPDATES = False
