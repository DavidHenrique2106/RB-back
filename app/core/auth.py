import jwt
from datetime import datetime, timedelta
from app.core.config import settings
import pytz

def criar_token_jwt(data: dict):
    expiracao = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({**data, "exp": expiracao}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        exp_timestamp = payload.get("exp")
        
        if exp_timestamp:
            exp_datetime = datetime.fromtimestamp(exp_timestamp, tz=pytz.UTC)
            
            if exp_datetime < datetime.utcnow().replace(tzinfo=pytz.UTC):
                return None
        
        return payload
    except jwt.ExpiredSignatureError:
        return None  
    except jwt.InvalidTokenError:
        return None  
