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
    op.bulk_insert(sa.table('building', sa.Column('address'), sa.Column('position')), [
        {'address': 'Блюхера, 32/1',     'position': '55°45′02″ с. ш. 37°37′03″ в. д.'}, # 1
        {'address': 'Маяковского, 28/1', 'position': '55°44′02″ с. ш. 37°38′03″ в. д.'}, # 2
        {'address': 'Ленина, 45',        'position': '55°46′02″ с. ш. 37°36′03″ в. д.'}, # 3
    ])

    op.bulk_insert(sa.table('organisation', sa.Column('name'), sa.Column('phone'), sa.Column('id_building')), [
        {'name': 'ООО “Рога и Копыта”', 'phone': '2-222-222, 3-333-333, 8-923-666-13-13', 'id_building': 1}, # 1
        {'name': 'ООО “Копыта и Рога”', 'phone': '3-333-333, 2-222-222, 8-923-666-13-13', 'id_building': 2}, # 2
    ])

    op.bulk_insert(sa.table('activity', sa.Column('name'), sa.Column('id_parent')), [
        {'name': 'Еда',                'id_parent': None}, # 1
        {'name': 'Мясная продукция',   'id_parent': 1   }, # 2
        {'name': 'Молочная продукция', 'id_parent': 1   }, # 3
        {'name': 'Автомобили',         'id_parent': None}, # 4
        {'name': 'Грузовые',           'id_parent': 4   }, # 5
        {'name': 'Легковые',           'id_parent': None}, # 6
        {'name': 'Запчасти',           'id_parent': 6   }, # 7
        {'name': 'Аксессуары',         'id_parent': 6   }, # 8
    ])

    op.bulk_insert(sa.table('link_org_act', sa.Column('id_org'), sa.Column('id_act')), [
        {'id_org': 1, 'id_act': 1},
        {'id_org': 1, 'id_act': 2},
        {'id_org': 2, 'id_act': 1},
        {'id_org': 2, 'id_act': 2},
    ])

def downgrade() -> None:
    pass
