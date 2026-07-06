from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Categoria
from app.schemas import CategoriaCreate, CategoriaResponse

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/", response_model= list[CategoriaResponse])
async def listar_categorias(db: AsyncSession = Depends(get_db)):
    resultado = await db.execute(select(Categoria))
    categoria = resultado.scalars().all()

    return categoria

@router.post("/", response_model= CategoriaResponse, status_code= 201)
async def criar_categoria(dados: CategoriaCreate, db: AsyncSession = Depends(get_db)):
    nova_categoria = Categoria(
        nome = dados.nome,
        cor = dados.cor,
        usuario_id = dados.usuario_id
    )

    db.add(nova_categoria)
    await db.commit()
    await db.refresh(nova_categoria)

    return nova_categoria

@router.put("/{categoria_id}", response_model= CategoriaResponse)
async def atualizar_categoria(categoria_id: int, dados: CategoriaCreate, db: AsyncSession = Depends(get_db)):
    categoria = await db.get(Categoria, categoria_id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

    categoria.nome = dados.nome
    categoria.cor = dados.cor

    await db.commit()
    await db.refresh(categoria)

    return categoria

@router.delete("/{categoria_id}", status_code= 204)
async def deletar_categoria(categoria_id: int, db: AsyncSession = Depends(get_db)):
    categoria = await db.get(Categoria, categoria_id)

    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    await db.delete(categoria)
    await db.commit()