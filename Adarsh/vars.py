# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '25835817)
    API_HASH = str(getenv('API_HASH', 'c461e309f9395cd31c64e27eaea5aee0'))
    BOT_TOKEN = str(getenv('BOT_TOKEN' '6846279662:AAET1oEFJqzVjCwbO9tJmZFfOC9UlxJvKrY'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002043373492'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '3.7.100.109'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5417967563").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'rm_gaming_ind'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '3.7.100.109:8080')) if not ON_HEROKU or getenv('FQDN', '3.7.100.109:8080') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'Monogodp link : mongodb+srv://rmajumdar532:<T6iV9wISQTjIpUNc>@cluster0.nqo1ses.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', '-1002127687196'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
