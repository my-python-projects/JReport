import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI    = os.getenv('MONGO_URI')
    MONGO_DBNAME = os.getenv('MONGO_DBNAME')
    SECRET_KEY   = os.getenv('SECRET_KEY', 'mysecretkey')