from bcrypt import hashpw, gensalt, checkpw
from jose import jwt, JWTError

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
EXPIRACAO_MINUTOS = 60

def hash_senha(senha: str) -> str:
    senha_bytes = senha.encode("utf-8")
    senha_hash = hashpw(senha_bytes, gensalt())
    senha_hash = senha_hash.decode()

    return senha_hash

def verificar_senha(senha: str, senha_hash: str) -> bool:
    senha_bytes_usuario = senha.encode("utf-8")
    senha_bytes_banco = senha_hash.encode("utf-8")

    return checkpw(senha_bytes_usuario, senha_bytes_banco)


def criar_token(usuario_id: int) -> str:
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=60)
    payload = {"sub": str(usuario_id), "exp": expiracao}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token

def decodificar_token(token: str) -> int | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id = payload.get("sub")
        return int(usuario_id)
    
    except JWTError:
        return None