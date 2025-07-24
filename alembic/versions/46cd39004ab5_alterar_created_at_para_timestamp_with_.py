"""Alterar created_at para timestamp with time zone

Revision ID: 46cd39004ab5
Revises: 6c7faa133fac
Create Date: 2025-07-23 16:03:13.746714

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46cd39004ab5'
down_revision: Union[str, Sequence[str], None] = '6c7faa133fac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE atletas
        ALTER COLUMN created_at TYPE TIMESTAMP WITH TIME ZONE
        USING created_at::text::timestamp with time zone;
    """)



def downgrade() -> None:
    op.execute("""
        ALTER TABLE atletas
        ALTER COLUMN created_at TYPE TIMETZ
        USING created_at::time;
    """)
