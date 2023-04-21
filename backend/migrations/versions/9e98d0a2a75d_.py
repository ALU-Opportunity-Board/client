"""empty message

Revision ID: 9e98d0a2a75d
Revises: 32f676c98c5f
Create Date: 2023-04-21 09:23:41.823643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e98d0a2a75d'
down_revision = '32f676c98c5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('phone_number')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.VARCHAR(length=50), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
