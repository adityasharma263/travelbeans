"""empty message

Revision ID: 01b29464ab8a
Revises: ac381923a139
Create Date: 2018-06-15 15:52:43.878077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01b29464ab8a'
down_revision = 'ac381923a139'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('website_room')
    op.add_column('website', sa.Column('room_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'website', 'room', ['room_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'website', type_='foreignkey')
    op.drop_column('website', 'room_id')
    op.create_table('website_room',
    sa.Column('website_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('room_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], name='website_room_room_id_fkey'),
    sa.ForeignKeyConstraint(['website_id'], ['website.id'], name='website_room_website_id_fkey'),
    sa.PrimaryKeyConstraint('website_id', 'room_id', name='website_room_pkey')
    )
    # ### end Alembic commands ###
