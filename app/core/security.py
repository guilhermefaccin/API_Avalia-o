import jwt
from passlib.context import cryptcontext
from config.Config import settings
from datetime import datetime, timezone

pwd_context = cryptcontext(schemes=["argon2"],deprecated="auto")

def criptografar_senha(senha:str):
    return pwd_context.hash(senha)

def verifica_senha(senha_plana:str,senha_banco:str):
    return pwd_context.verify(senha_plana,senha_banco)

def criar_token(id_usuario:str,Usuario_Status:list[str]):
    vence_em = datetime.now(timezone.utc)+settings.JWT_ACCESS_EXPIRE_MINUTES
    payload ={"sub":id_usuario,"exp":vence_em,"Usuario_Status":Usuario_Status,"iss":settings.JWT_ISSUER}
    token = jwt.encode(payload,settings.JWT_SECRET_KEY,settings.JWT_ALGORITHM)
    return token