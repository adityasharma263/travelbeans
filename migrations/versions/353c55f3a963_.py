"""empty message

Revision ID: 353c55f3a963
Revises: 017cfc7d8974
Create Date: 2018-07-14 22:10:35.650691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '353c55f3a963'
down_revision = '017cfc7d8974'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('category', sa.Integer(), nullable=True))
    op.drop_column('restaurant', 'Category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('Category', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('restaurant', 'category')
    # ### end Alembic commands ###
