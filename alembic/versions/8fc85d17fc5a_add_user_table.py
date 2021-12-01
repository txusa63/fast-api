"""add user table

Revision ID: 8fc85d17fc5a
Revises: b8d27d2cc71c
Create Date: 2021-12-01 12:25:56.332765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fc85d17fc5a'
down_revision = 'b8d27d2cc71c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',sa.Column('id', sa.Integer(), nullable=False),
                            sa.Column('email', sa.String(), nullable=False),
                            sa.Column('password', sa.String(), nullable=False),
                            sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                    server_default=sa.text('now()'), nullable=False),
                            sa.PrimaryKeyConstraint('id'),
                            sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
