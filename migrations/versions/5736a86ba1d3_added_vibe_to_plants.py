"""added vibe to plants

Revision ID: 5736a86ba1d3
Revises: fffc6013f9a4
Create Date: 2024-02-17 17:02:39.168186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5736a86ba1d3'
down_revision = 'fffc6013f9a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plant', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vibes', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plant', schema=None) as batch_op:
        batch_op.drop_column('vibes')

    # ### end Alembic commands ###
