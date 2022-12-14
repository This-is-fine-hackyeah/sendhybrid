"""Rename orientation to size

Revision ID: 52e143908bb2
Revises: 34298b352974
Create Date: 2022-11-20 05:18:14.634820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52e143908bb2'
down_revision = '34298b352974'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('report', sa.Column('size', sa.Boolean(), nullable=True))
    op.drop_column('report', 'orientation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('report', sa.Column('orientation', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('report', 'size')
    # ### end Alembic commands ###
