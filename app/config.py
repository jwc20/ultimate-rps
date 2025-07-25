from dotenv import load_dotenv

import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM =  os.getenv("ALGORITHM") 
ACCESS_TOKEN_EXPIRE_MINUTES = 30

REDIS_URL = os.getenv("REDIS_URL")

# DATABASE_URL="sqlite:///database.db"
DATABASE_URL = os.getenv("DATABASE_URL")