"""Missing column in Venue and Artist and creation of shows: the association table.

Revision ID: 544f0165aaf1
Revises: 255dca8063f3
Create Date: 2022-08-14 15:34:40.422658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '544f0165aaf1'
down_revision = '255dca8063f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Show',
    sa.Column('Artist_id', sa.Integer(), nullable=False),
    sa.Column('Venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['Artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['Venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('Artist_id', 'Venue_id')
    )
    op.add_column('Artist', sa.Column('web_link', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('looking_for_talent', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('web_link', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('looking_for_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'looking_for_talent')
    op.drop_column('Venue', 'web_link')
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'looking_for_talent')
    op.drop_column('Artist', 'web_link')
    op.drop_table('Show')
    # ### end Alembic commands ###
