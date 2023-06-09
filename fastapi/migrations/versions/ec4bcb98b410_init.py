"""add user

Revision ID: ec4bcb98b410
Revises: 6a7dcd1e227e
Create Date: 2023-05-12 12:03:24.356217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec4bcb98b410'
down_revision = '6a7dcd1e227e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('refresh_token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('contacts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contacts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_column('contacts', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###