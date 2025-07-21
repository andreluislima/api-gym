
from workout_api.contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, Integer, String, Float
from datetime import datetime

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer, primary_Key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    idade:Mapped[int] = mapped_column(Integer, nullable=False)
    peso:Mapped[float] = mapped_column(Float, nullable=False)
    altura:Mapped[Float] = mapped_column(Float, nullable=False)
    genero:Mapped[str] = mapped_column(String, nullable=False)
    created_at:Mapped[datetime] = mapped_column(DateTime, nullable=False)