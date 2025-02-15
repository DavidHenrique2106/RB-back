import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    PORT = int(os.getenv("PORT", 10000))
    ENV = os.getenv("ENV", "dev")
    
    if ENV == "prod":
        FRONTEND_URL = os.getenv("FRONTEND_URL_PROD")
    else:
        FRONTEND_URL = os.getenv("FRONTEND_URL_DEV")

settings = Settings()
