from fastapi import FastAPI
from app.routers import auth, usuarios, categorias, transacoes

app = FastAPI(title="Controle Financeiro")

app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(categorias.router)
app.include_router(transacoes.router)