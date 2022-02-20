"""add user table

Revision ID: 28b2ff3fa6fa
Revises: 66e5ec79630a
Create Date: 2022-02-19 21:16:23.093763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28b2ff3fa6fa'
down_revision = '66e5ec79630a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), 
                             sa.Column('email', sa.String(), nullable=False),
                             sa.Column('password', sa.String(), nullable=False),
                             sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                             sa.PrimaryKeyConstraint('id'),
                             sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
