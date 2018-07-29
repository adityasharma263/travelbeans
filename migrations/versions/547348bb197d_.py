"""empty message

Revision ID: 547348bb197d
Revises: 412d5e371a0c
Create Date: 2018-07-29 17:11:32.273707

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '547348bb197d'
down_revision = '412d5e371a0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    op.drop_table('association')
    op.drop_constraint('cab_booking_cab_id_key', 'cab_booking', type_='unique')
    op.create_unique_constraint(None, 'cab_invoice', ['booking_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cab_invoice', type_='unique')
    op.create_unique_constraint('cab_booking_cab_id_key', 'cab_booking', ['cab_id'])
    op.create_table('association',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('restaurant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('dish_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('collection_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cuisine_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['collection_id'], ['collection.id'], name='association_collection_id_fkey'),
    sa.ForeignKeyConstraint(['cuisine_id'], ['cuisine.id'], name='association_cuisine_id_fkey'),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], name='association_dish_id_fkey'),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], name='association_restaurant_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='association_pkey')
    )
    op.create_table('tag',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('restaurant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('breakfast', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('lunch', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('dinner', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('cafe', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('lounge', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('family', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('bars', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('nightlife', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('street_stalls', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('pocket_friendly', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('diet', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('luxury', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], name='tag_restaurant_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='tag_pkey'),
    sa.UniqueConstraint('restaurant_id', name='tag_restaurant_id_key')
    )
    # ### end Alembic commands ###
