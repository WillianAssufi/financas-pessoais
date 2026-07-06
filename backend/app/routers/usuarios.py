from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

from app.database import get_db
from app.models import Usuario
from app.schemas import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from app.security import hash_senha

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/", response_model= list[UsuarioResponse])
async def listar_usuarios(db: AsyncSession = Depends(get_db)):
    resultado = await db.execute(select(Usuario))
    usuario = resultado.scalars().all()

    return usuario

@router.post("/", response_model= UsuarioResponse, status_code= 201)
async def criar_usuario(dados: UsuarioCreate, db: AsyncSession = Depends(get_db)):
    novo_usuario = Usuario(
        nome = dados.nome,
        email = dados.email,
        senha_hash = hash_senha(dados.senha)
    )

    db.add(novo_usuario)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=409, detail="Email já cadastrado")
    await db.refresh(novo_usuario)

    return novo_usuario

@router.put("/{usuario_id}", response_model= UsuarioResponse)
async def atualizar_usuario(usuario_id: int, dados: UsuarioUpdate, db: AsyncSession = Depends(get_db)):
    usuario = await db.get(Usuario, usuario_id)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    if dados.nome is not None:
        usuario.nome = dados.nome

    if dados.email is not None:
        usuario.email = dados.email

    if dados.senha is not None:
        usuario.senha_hash = hash_senha(dados.senha)
    
    await db.commit()
    await db.refresh(usuario)

    return usuario

@router.delete("/{usuario_id}", status_code= 204)
async def deletar_usuario(usuario_id: int, db: AsyncSession = Depends(get_db)):
    usuario = await db.get(Usuario, usuario_id)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    await db.delete(usuario)
    await db.commit()
    
