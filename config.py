from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "20272463"))
API_HASH = getenv("API_HASH", "4044459cd2988126c15d628b1d67a25a")
BOT_TOKEN = getenv("BOT_TOKEN", "5557419876:AAH1qlp8lpwj7m4heK9cFDDlHBPX-FySgH0")
SESSION_NAME = getenv("SESSION_NAME", "BAAoeWh3yBv2cWH4JcBhbifnw-XlEnMvPnAbBKfJB9Uy17kuThto_bpKfRGttSRPwRrDK9AIxSNXP6vj8dOGVTJ46JYdkBZHMXXXpcGEGXbROg5Tf8IiDgh5PwcILauRHbtOPuHYmadbcTeVryhofsqYfPet-myQ3-yP2OKjs10hKa935uPLznQja0DM87L7O3NxjJGaRznWOmY7_0nC_sqF_Xm3mGF93jtLGlobqFHYXDN7O92ZtPCDvc3fjx8Hr8_LsZWNbgnbl8Jr10zAnOmxp8JP3-ZuiijrrfDRc23GKB3tT6n4j20ZI9ZyEHr93y4RkdvQxlmK3a0PCacBqrX0AAAAAVvrVAkA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "BotDarbakaabnbott")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "BotDarbakaabnbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VV_OG")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
