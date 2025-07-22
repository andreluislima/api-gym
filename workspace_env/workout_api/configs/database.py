from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from workout_api.configs.settings import settings

# Cria o motor de conexão assíncrono
engine = create_async_engine(settings.DB_URL, echo=False)

# Usa o async_sessionmaker ao invés do sessionmaker tradicional
async_session = async_sessionmaker(
    bind=engine,  # aqui o tipo já é aceito
    class_=AsyncSession,
    expire_on_commit=False
)

# Função de dependência com yield para FastAPI
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
