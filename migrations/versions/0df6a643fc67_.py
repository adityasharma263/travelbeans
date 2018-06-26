"""empty message

Revision ID: 0df6a643fc67
Revises: 4b05cee801e8
Create Date: 2018-06-26 16:56:07.080229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0df6a643fc67'
down_revision = '4b05cee801e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('amenity', sa.Column('couple_friendly', sa.Boolean(), nullable=True))
    op.add_column('amenity', sa.Column('parking', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('amenity', 'parking')
    op.drop_column('amenity', 'couple_friendly')
    # ### end Alembic commands ###
