"""add content column to posts table

Revision ID: 66e5ec79630a
Revises: 7eb8268a9191
Create Date: 2022-02-19 21:10:07.666094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66e5ec79630a'
down_revision = '7eb8268a9191'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
