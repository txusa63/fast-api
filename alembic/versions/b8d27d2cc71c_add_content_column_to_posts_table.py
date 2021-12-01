"""add content column to posts table

Revision ID: b8d27d2cc71c
Revises: ae9cf3387f8e
Create Date: 2021-12-01 10:05:44.702613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8d27d2cc71c'
down_revision = 'ae9cf3387f8e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
