from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Usuario
from app.security import verificar_senha, criar_token

router = APIRouter(tags=["Autenticação"])

@router.post("/login")
async def autenticar(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    resultado = await db.execute(select(Usuario).where(Usuario.email == form_data.username))
    usuario = resultado.scalar_one_or_none()

    if not usuario or not verificar_senha(form_data.password, usuario.senha_hash):
        raise HTTPException(status_code= 401, detail= "Usuário ou senha não existem ou estão incorretos")
    
    token = criar_token(usuario.id)
    
    return {"access_token": token, "token_type": "bearer"}