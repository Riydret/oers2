"""empty message

Revision ID: c7ee0a472f0c
Revises: 46e6e4057acd
Create Date: 2018-08-20 07:30:48.040621

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c7ee0a472f0c'
down_revision = '46e6e4057acd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('equipment', 'quantity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('equipment', sa.Column('quantity', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
