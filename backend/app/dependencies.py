from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Usuario
from app.security import decodificar_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_usuario_atual(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    usuario_id = decodificar_token(token)

    if usuario_id is None:
        raise HTTPException(status_code= 401, detail= "Token inválido ou expirado")
    
    resultado = await db.execute(select(Usuario).where(Usuario.id == usuario_id))
    usuario = resultado.scalar_one_or_none()

    if usuario is None:
        raise HTTPException(status_code= 401, detail= "Usuário não encontrado")
    
    return usuario