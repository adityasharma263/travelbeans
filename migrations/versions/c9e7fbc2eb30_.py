"""empty message

Revision ID: c9e7fbc2eb30
Revises: 03eb40bf2997
Create Date: 2018-08-20 00:28:40.482994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9e7fbc2eb30'
down_revision = '03eb40bf2997'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cab_collection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('collection_name', sa.String(), nullable=True),
    sa.Column('featured', sa.Boolean(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cab_collection_id'), 'cab_collection', ['id'], unique=False)
    op.create_table('cab_collection_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('cab_collection_id', sa.Integer(), nullable=False),
    sa.Column('product_url', sa.String(), nullable=True),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.Column('featured_product', sa.Boolean(), nullable=True),
    sa.Column('product_desc', sa.Text(), nullable=True),
    sa.Column('product_image', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cab_collection_id'], ['cab_collection.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cab_collection_product_id'), 'cab_collection_product', ['id'], unique=False)
    op.add_column('cab', sa.Column('collection_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cab', 'cab_collection', ['collection_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cab', type_='foreignkey')
    op.drop_column('cab', 'collection_id')
    op.drop_index(op.f('ix_cab_collection_product_id'), table_name='cab_collection_product')
    op.drop_table('cab_collection_product')
    op.drop_index(op.f('ix_cab_collection_id'), table_name='cab_collection')
    op.drop_table('cab_collection')
    # ### end Alembic commands ###