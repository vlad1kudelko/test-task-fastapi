"""seeding

Revision ID: a5ee90dc0d72
Revises: 0dcde0c034cf
Create Date: 2025-01-25 13:50:40.382692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a5ee90dc0d72'
down_revision: Union[str, None] = '0dcde0c034cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    my_table = sa.table('organisation',
        sa.column('name', String)
        sa.column('phone', String)
    )

    op.bulk_insert(my_table, [
        {'name': 'Item 1', 'phone': '89992223344'},
        {'name': 'Item 2', 'phone': '89992223344'},
        {'name': 'Item 3', 'phone': '89992223344'},
    ])

def downgrade() -> None:
    pass
