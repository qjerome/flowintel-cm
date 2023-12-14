"""empty message

Revision ID: 73b8cc4d3c54
Revises: c42cd6e3e1ea
Create Date: 2023-12-07 10:05:44.775815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73b8cc4d3c54'
down_revision = 'c42cd6e3e1ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('expanded', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_column('expanded')
        batch_op.drop_column('description')

    # ### end Alembic commands ###