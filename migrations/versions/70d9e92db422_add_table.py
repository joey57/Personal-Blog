"""add table

Revision ID: 70d9e92db422
Revises: a693a8baf0cb
Create Date: 2022-05-14 12:57:19.436519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70d9e92db422'
down_revision = 'a693a8baf0cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###