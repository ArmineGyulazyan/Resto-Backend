"""Change column name

Revision ID: 327c75080602
Revises: 
Create Date: 2024-04-07 14:53:40.869443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '327c75080602'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pastas_addition', table_name='pastas')
    op.drop_index('ix_pastas_description', table_name='pastas')
    op.drop_index('ix_pastas_name', table_name='pastas')
    op.drop_index('ix_pastas_pasta_type', table_name='pastas')
    op.drop_index('ix_pastas_portion', table_name='pastas')
    op.drop_index('ix_pastas_price', table_name='pastas')
    op.drop_index('ix_pastas_time', table_name='pastas')
    op.drop_table('pastas')
    op.drop_index('ix_drinks_description', table_name='drinks')
    op.drop_index('ix_drinks_name', table_name='drinks')
    op.drop_index('ix_drinks_price', table_name='drinks')
    op.drop_index('ix_drinks_size', table_name='drinks')
    op.drop_index('ix_drinks_type', table_name='drinks')
    op.drop_table('drinks')
    # ### end Alembic commands ###
    op.alter_column('drinks', 'id', new_column_name='id_')
    op.alter_column('drinks', 'type', new_column_name='drink_type')
    op.alter_column('pastas', 'id', new_column_name='id_')

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drinks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('type', sa.VARCHAR(), nullable=True),
    sa.Column('size', sa.FLOAT(), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_drinks_type', 'drinks', ['type'], unique=False)
    op.create_index('ix_drinks_size', 'drinks', ['size'], unique=False)
    op.create_index('ix_drinks_price', 'drinks', ['price'], unique=False)
    op.create_index('ix_drinks_name', 'drinks', ['name'], unique=False)
    op.create_index('ix_drinks_description', 'drinks', ['description'], unique=False)
    op.create_table('pastas',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('pasta_type', sa.VARCHAR(), nullable=True),
    sa.Column('portion', sa.INTEGER(), nullable=True),
    sa.Column('addition', sa.VARCHAR(), nullable=True),
    sa.Column('time', sa.INTEGER(), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_pastas_time', 'pastas', ['time'], unique=False)
    op.create_index('ix_pastas_price', 'pastas', ['price'], unique=False)
    op.create_index('ix_pastas_portion', 'pastas', ['portion'], unique=False)
    op.create_index('ix_pastas_pasta_type', 'pastas', ['pasta_type'], unique=False)
    op.create_index('ix_pastas_name', 'pastas', ['name'], unique=False)
    op.create_index('ix_pastas_description', 'pastas', ['description'], unique=False)
    op.create_index('ix_pastas_addition', 'pastas', ['addition'], unique=False)
    # ### end Alembic commands ###
