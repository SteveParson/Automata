import os

import motor.motor_asyncio
import sentry_sdk

DISABLED_PLUGINS = os.getenv("AUTOMATA_DISABLED_PLUGINS", "").split(",")

PRIMARY_GUILD = int(os.getenv("AUTOMATA_PRIMARY_GUILD", 514110851016556567))
VERIFIED_ROLE = int(os.getenv("AUTOMATA_VERIFIED_ROLE", 564672793380388873))

EXECUTIVE_DOCS_CHANNEL = int(
    os.getenv("AUTOMATA_EXECUTIVE_DOCS_CHANNEL", 773246740002373652)
)

DIARY_DAILY_CHANNEL = int(os.getenv("AUTOMATA_DIARY_DAILY_CHANNEL", 872217138851614750))

NEWSLINE_CHANNEL = int(os.getenv("AUTOMATA_NEWSLINE_CHANNEL", 811433377642446869))

WHITELIST_HTTP_API_BEARER_TOKEN = os.getenv("WHITELIST_HTTP_API_BEARER_TOKEN", None)

MONGO_HOST = os.getenv("AUTOMATA_MONGO_HOST", "mongo")
MONGO_ADDRESS = f"mongodb://{MONGO_HOST}/automata"

DISCORD_AUTH_URI = os.getenv("DISCORD_AUTH_URI", "https://discord.muncompsci.ca")

WEATHER_API_KEY = os.getenv("AUTOMATA_WEATHER_API_KEY")

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_ADDRESS)

if os.getenv("SENTRY_DSN", None):
    sentry_sdk.init(os.environ["SENTRY_DSN"])
