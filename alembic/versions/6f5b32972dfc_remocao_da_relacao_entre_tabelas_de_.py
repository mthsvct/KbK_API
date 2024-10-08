"""Remocao da relacao entre tabelas de endereco

Revision ID: 6f5b32972dfc
Revises: c9b33094b955
Create Date: 2024-05-19 18:00:37.960353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f5b32972dfc'
down_revision: Union[str, None] = 'c9b33094b955'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.drop_constraint('fk_cliente_endereco', type_='foreignkey')

    with op.batch_alter_table('funcionario', schema=None) as batch_op:
        batch_op.drop_constraint('fk_funcionario_endereco', type_='foreignkey')

    with op.batch_alter_table('salao', schema=None) as batch_op:
        batch_op.drop_constraint('fk_salao_endereco', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salao', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_salao_endereco', 'endereco', ['endereco_id'], ['id'])

    with op.batch_alter_table('funcionario', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_funcionario_endereco', 'endereco', ['endereco_id'], ['id'])

    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_cliente_endereco', 'endereco', ['endereco_id'], ['id'])

    # ### end Alembic commands ###
