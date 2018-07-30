"""empty message

Revision ID: 7d58800f4200
Revises: e2622962140b
Create Date: 2018-07-29 18:32:28.931660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d58800f4200'
down_revision = 'e2622962140b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cab_website',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('logo_image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cab_website_id'), 'cab_website', ['id'], unique=False)
    op.add_column('cab_invoice', sa.Column('website_id', sa.Integer(), nullable=True))
    op.drop_constraint('cab_invoice_booking_id_key', 'cab_invoice', type_='unique')
    op.create_foreign_key(None, 'cab_invoice', 'cab_website', ['website_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cab_invoice', type_='foreignkey')
    op.create_unique_constraint('cab_invoice_booking_id_key', 'cab_invoice', ['booking_id'])
    op.drop_column('cab_invoice', 'website_id')
    op.drop_index(op.f('ix_cab_website_id'), table_name='cab_website')
    op.drop_table('cab_website')
    # ### end Alembic commands ###
