from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Transacao, Usuario
from app.schemas import TransacaoCreate, TransacaoResponse
from app.dependencies import get_usuario_atual

router = APIRouter(prefix="/transacoes", tags=["Transações"])

@router.get("/", response_model= list[TransacaoResponse])
async def listar_transacoes(usuario_atual: Usuario = Depends(get_usuario_atual), db: AsyncSession = Depends(get_db)):
    resultado = await db.execute(select(Transacao).where(Transacao.usuario_id == usuario_atual.id))
    transacao = resultado.scalars().all()

    return transacao
   
@router.post("/", response_model= TransacaoResponse, status_code=201)
async def criar_transacao(dados: TransacaoCreate, usuario_atual: Usuario = Depends(get_usuario_atual), db: AsyncSession = Depends(get_db)):
    nova_transacao = Transacao(
        descricao = dados.descricao,
        valor = dados.valor,
        tipo = dados.tipo,
        data = dados.data,
        usuario_id = usuario_atual.id,
        categoria_id = dados.categoria_id
    )

    db.add(nova_transacao)
    await db.commit()
    await db.refresh(nova_transacao)

    return nova_transacao


@router.put("/{transacao_id}", response_model=TransacaoResponse)
async def atualizar_transacao(transacao_id: int, dados: TransacaoCreate, usuario_atual: Usuario = Depends(get_usuario_atual), db: AsyncSession = Depends(get_db)):
    resultado = await db.execute(select(Transacao).where(Transacao.id == transacao_id,Transacao.usuario_id == usuario_atual.id))
    transacao = resultado.scalar_one_or_none()  

    if transacao is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    
    transacao.descricao = dados.descricao
    transacao.valor = dados.valor
    transacao.tipo = dados.tipo
    transacao.data = dados.data

    await db.commit()
    await db.refresh(transacao)

    return transacao

@router.delete("/{transacao_id}", status_code= 204)
async def deletar_transacao(transacao_id: int, usuario_atual: Usuario = Depends(get_usuario_atual), db: AsyncSession = Depends(get_db)):
    resultado = await db.execute(select(Transacao).where(Transacao.id == transacao_id,Transacao.usuario_id == usuario_atual.id))
    transacao = resultado.scalar_one_or_none() 

    if transacao is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    
    await db.delete(transacao)
    await db.commit()