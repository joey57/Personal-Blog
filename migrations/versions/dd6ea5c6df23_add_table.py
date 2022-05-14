"""Add table

Revision ID: dd6ea5c6df23
Revises: 3c579fc08170
Create Date: 2022-05-14 17:58:58.665086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd6ea5c6df23'
down_revision = '3c579fc08170'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=200), nullable=False),
    sa.Column('author', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###