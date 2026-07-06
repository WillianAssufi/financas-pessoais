from pydantic import BaseModel, EmailStr
from typing import Literal

from decimal import Decimal
from datetime import date

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True

class UsuarioUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    senha: str | None = None

class CategoriaCreate(BaseModel):
    nome: str
    cor: str
    usuario_id: int

class CategoriaResponse(BaseModel):
    id: int
    nome: str
    cor: str
    usuario_id: int

    class Config:
        from_attributes = True

class TransacaoCreate(BaseModel):
    descricao: str
    valor: Decimal
    tipo: Literal["receita", "despesa"]
    data: date
    categoria_id: int

class TransacaoResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: Literal["receita", "despesa"]
    data: date
    usuario_id: int
    categoria_id: int

    class Config:
        from_attributes = True

