"""20160530 users add column avatar_hash

Revision ID: cb48a710adbc
Revises: df69befd5054
Create Date: 2016-05-30 23:07:55.535449

"""

# revision identifiers, used by Alembic.
revision = 'cb48a710adbc'
down_revision = 'df69befd5054'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
