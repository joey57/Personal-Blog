"""add tables

Revision ID: a227a6ecf18c
Revises: 77e2c786170d
Create Date: 2022-05-13 18:29:29.927429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a227a6ecf18c'
down_revision = '77e2c786170d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.drop_index('ix_users_username', table_name='users')
    op.create_unique_constraint(None, 'users', ['username'])
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###