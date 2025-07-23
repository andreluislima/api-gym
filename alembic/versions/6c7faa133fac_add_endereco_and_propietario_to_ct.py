"""add endereco and propietario to CT

Revision ID: 6c7faa133fac
Revises: aca05d8e458d
Create Date: 2025-07-23 15:18:34.312718
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c7faa133fac'
down_revision: Union[str, Sequence[str], None] = 'aca05d8e458d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Passo 1: adiciona as colunas como nullable=True (temporariamente)
    op.add_column('centros_treinamento', sa.Column('endereco', sa.String(length=60), nullable=True))
    op.add_column('centros_treinamento', sa.Column('propietario', sa.String(length=30), nullable=True))

    # Passo 2: preenche os valores nulos com um valor padrão
    op.execute("UPDATE centros_treinamento SET endereco = 'indefinido' WHERE endereco IS NULL")
    op.execute("UPDATE centros_treinamento SET propietario = 'admin' WHERE propietario IS NULL")

    # Passo 3: torna as colunas NOT NULL
    op.alter_column('centros_treinamento', 'endereco', nullable=False)
    op.alter_column('centros_treinamento', 'propietario', nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('centros_treinamento', 'propietario')
    op.drop_column('centros_treinamento', 'endereco')
