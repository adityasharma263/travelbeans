"""empty message

Revision ID: b2eb3d6db1bd
Revises: 303120bc6c13
Create Date: 2018-08-23 17:47:55.177973

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b2eb3d6db1bd'
down_revision = '303120bc6c13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cab_tax')
    op.drop_table('cab_booking')
    op.drop_table('cab_user')
    op.drop_column('cab', 'is_partner')
    op.add_column('cab_deal', sa.Column('is_partner', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cab_deal', 'is_partner')
    op.add_column('cab', sa.Column('is_partner', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.create_table('cab_user',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('cab_user_id_seq'::regclass)"), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cab_user_pkey'),
    sa.UniqueConstraint('email', name='cab_user_email_key'),
    sa.UniqueConstraint('phone', name='cab_user_phone_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('cab_booking',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('pickup_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('drop_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('drop_latitude', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('drop_longitude', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('pickup_latitude', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('pickup_longitude', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('cab_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('deal_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('booking_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('booking_status', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cab_booking_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('mode_of_payment', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total_distance', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('total_fare', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('total_hours', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('total_days', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cab_id'], ['cab.id'], name='cab_booking_cab_id_fkey'),
    sa.ForeignKeyConstraint(['deal_id'], ['cab_deal.id'], name='cab_booking_deal_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['cab_user.id'], name='cab_booking_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='cab_booking_pkey')
    )
    op.create_table('cab_tax',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('gst', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('s_gst', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('c_gst', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('booking_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('i_gst', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['booking_id'], ['cab_booking.id'], name='cab_tax_booking_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='cab_tax_pkey'),
    sa.UniqueConstraint('booking_id', name='cab_tax_booking_id_key')
    )
    # ### end Alembic commands ###