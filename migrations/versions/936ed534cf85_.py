"""empty message

Revision ID: 936ed534cf85
Revises: 43cfdf0f229c
Create Date: 2018-08-05 13:20:45.427008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '936ed534cf85'
down_revision = '43cfdf0f229c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cuisine', sa.Column('desc', sa.Text(), nullable=True))
    op.add_column('cuisine', sa.Column('featured', sa.Boolean(), nullable=True))
    op.add_column('cuisine', sa.Column('image', sa.String(), nullable=True))
    op.add_column('restaurant', sa.Column('locality', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurant', 'locality')
    op.drop_column('cuisine', 'image')
    op.drop_column('cuisine', 'featured')
    op.drop_column('cuisine', 'desc')
    # ### end Alembic commands ###
