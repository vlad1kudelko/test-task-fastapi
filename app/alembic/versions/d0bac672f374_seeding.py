"""seeding

Revision ID: d0bac672f374
Revises: 2611edc3eaf7
Create Date: 2025-01-26 06:33:52.018198

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0bac672f374'
down_revision: Union[str, None] = '2611edc3eaf7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(sa.table('building', sa.Column('address'), sa.Column('position_x'), sa.Column('position_y')), [
        {'address': 'Блюхера, 32/1',     'position_x': 55.717435, 'position_y': 37.561014}, # 1
        {'address': 'Маяковского, 28/1', 'position_x': 55.711333, 'position_y': 37.561858}, # 2
        {'address': 'Ленина, 45',        'position_x': 55.713216, 'position_y': 37.550191}, # 3
    ])

    op.bulk_insert(sa.table('organisation', sa.Column('name'), sa.Column('phone'), sa.Column('id_building')), [
        {'name': 'ООО “Рога и Копыта”', 'phone': '2-222-222, 3-333-333, 8-923-666-13-13', 'id_building': 1}, # 1
        {'name': 'ИП “Рога”',           'phone': '2-222-222, 3-333-333, 8-923-666-13-13', 'id_building': 1}, # 2
        {'name': 'ООО “Копыта и Рога”', 'phone': '3-333-333, 2-222-222, 8-923-666-13-13', 'id_building': 2}, # 3
        {'name': 'ИП “Копыта”',         'phone': '2-222-222, 3-333-333, 8-923-666-13-13', 'id_building': 2}, # 4
    ])

    op.bulk_insert(sa.table('activity', sa.Column('name'), sa.Column('id_parent')), [
        {'name': 'Еда',                'id_parent': None}, # 1
        {'name': 'Мясная продукция',   'id_parent': 1   }, # 2
        {'name': 'Молочная продукция', 'id_parent': 1   }, # 3
        {'name': 'Автомобили',         'id_parent': None}, # 4
        {'name': 'Грузовые',           'id_parent': 4   }, # 5
        {'name': 'Легковые',           'id_parent': 4   }, # 6
        {'name': 'Запчасти',           'id_parent': 6   }, # 7
        {'name': 'Аксессуары',         'id_parent': 6   }, # 8
    ])

    op.bulk_insert(sa.table('link_org_act', sa.Column('id_org'), sa.Column('id_act')), [
        {'id_org': 1, 'id_act': 1},
        {'id_org': 1, 'id_act': 2},
        {'id_org': 2, 'id_act': 3},
        {'id_org': 2, 'id_act': 4},
        {'id_org': 3, 'id_act': 1},
        {'id_org': 3, 'id_act': 2},
        {'id_org': 4, 'id_act': 3},
        {'id_org': 4, 'id_act': 4},
    ])


def downgrade() -> None:
    pass
