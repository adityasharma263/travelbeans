"""empty message

Revision ID: 03eb40bf2997
Revises: 1f7e6271b1c9
Create Date: 2018-08-19 15:39:54.790529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03eb40bf2997'
down_revision = '1f7e6271b1c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('website', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurant', 'website')
    # ### end Alembic commands ###
