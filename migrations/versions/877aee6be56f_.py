"""empty message

Revision ID: 877aee6be56f
Revises: 1807e368887b
Create Date: 2018-09-05 03:08:41.197250

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '877aee6be56f'
down_revision = '1807e368887b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('facilityPropertyNumber', table_name='facility')
    op.drop_column('facility', 'facilityPropertyNumber')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('facility', sa.Column('facilityPropertyNumber', mysql.VARCHAR(length=50), nullable=False))
    op.create_index('facilityPropertyNumber', 'facility', ['facilityPropertyNumber'], unique=True)
    # ### end Alembic commands ###
