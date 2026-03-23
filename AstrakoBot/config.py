import os

class Development:
    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
    TOKEN = os.environ.get("API_KEY", "")

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", "")
    EVENT_LOGS = os.environ.get("EVENT_LOGS", "")
    USE_JOIN_LOGGER = True

    WEBHOOK = False   # 🔥 important fix

    ALLOW_CHATS = True

    DEV_USERS = []
    SUPPORT_USERS = []
    SUDO_USERS = []
    WHITELIST_USERS = []

    LOAD = []
    NO_LOAD = []
