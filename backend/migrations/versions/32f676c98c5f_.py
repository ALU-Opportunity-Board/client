"""empty message

Revision ID: 32f676c98c5f
Revises: 
Create Date: 2023-04-21 08:42:05.532636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32f676c98c5f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('role', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('opportunities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('opportunity_type', sa.String(length=100), nullable=False),
    sa.Column('field', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('link', sa.String(length=400), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('opportunities')
    op.drop_table('users')
    # ### end Alembic commands ###
