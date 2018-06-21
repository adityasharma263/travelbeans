"""empty message

Revision ID: 318f1c63df45
Revises: 56f8c3edcec8
Create Date: 2018-06-22 01:45:32.361630

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '318f1c63df45'
down_revision = '56f8c3edcec8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('hotel_url', sa.String(), nullable=True),
    sa.Column('weekend', sa.Boolean(), nullable=False),
    sa.Column('hotel_id', sa.Integer(), nullable=True),
    sa.Column('website_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotel.id'], ),
    sa.ForeignKeyConstraint(['website_id'], ['website.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deal_id'), 'deal', ['id'], unique=False)
    op.drop_table('price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('price',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hotel_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('website_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('weekend', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['hotel_id'], ['hotel.id'], name='price_hotel_id_fkey'),
    sa.ForeignKeyConstraint(['website_id'], ['website.id'], name='price_website_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='price_pkey')
    )
    op.drop_index(op.f('ix_deal_id'), table_name='deal')
    op.drop_table('deal')
    # ### end Alembic commands ###
