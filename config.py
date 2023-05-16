
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6296295298:AAG82Ph5DQjGVKwg4vSUyNyuLaW3YXL4A7E")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "26861990"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "0592761ae3a24dcf709d85ab87bc12b9")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQGZ4aYAb7SbzAcwkRxG_ICO_fcDZMR6BIO3vIKApsfqKWJT-2-_oaEVmxn1CXvx-hi9s14_ennY0WMclgKkTQaFT-aQqN4HSt5BdRQJ6B99Er0pmAR5iij29Axu0RGVP8Zf3YqX7_hHFxYKkPm0MwpEjGvRNQT8ZqQssm2mcMF1O2sM5CI3YA7JgkYuOJeDKtNiyOXr0Y_kKp-tQaiUYkFq-D1jrHoNzHS2oMBU77b10gFiZHIBDD0kd4x9-17HB4OG-33qjcMMUPbFv-dkpYDueIX8HerB0v2yb6OItXiXq7rAuJX_mj5-yGt_eOSq275A4iMUDH1DzeM4WAAaiB4QZAIXvwAAAAFnifBOAA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "1001847058383")
TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

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
