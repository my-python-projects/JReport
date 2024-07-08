import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI       = os.getenv('MONGO_URI')
    MONGO_DBNAME    = os.getenv('MONGO_DBNAME')
    SECRET_KEY      = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY  = os.getenv('JWT_SECRET_KEY')
    # SECRET_KEY  = os.getenv('SECRET_KEY', os.urandom(24).hex())
    # JWT_SECRET_KEY  = os.getenv('JWT_SECRET_KEY', os.urandom(24).hex())
    JWT_ACCESS_TOKEN_EXPIRES    = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # 1 hora
    JWT_REFRESH_TOKEN_EXPIRES   = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', 86400))  # 1 dia