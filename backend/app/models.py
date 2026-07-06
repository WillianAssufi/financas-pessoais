from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Date, Numeric

from decimal import Decimal
from datetime import date

from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(150), unique=True)
    senha_hash: Mapped[str] = mapped_column(String(255))

class Categoria(Base):
    __tablename__ = "categorias"
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id", ondelete="CASCADE"))
    nome: Mapped[str] = mapped_column(String(50))
    cor: Mapped[str] = mapped_column(String(7))

class Transacao(Base):
    __tablename__ = "transacoes"
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id", ondelete="CASCADE"))
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id", ondelete="CASCADE"))
    descricao: Mapped[str] = mapped_column(String(100))
    valor: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    tipo: Mapped[str] = mapped_column(String(20))
    data: Mapped[date] = mapped_column(Date)


    