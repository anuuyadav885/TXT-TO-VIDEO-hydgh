# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("API_ID", "24509126"))
API_HASH = environ.get("API_HASH", "2c1e3e02b9e1b0a3f9c7955d5d55a1d5")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
