"""empty message

Revision ID: 819665adf2f8
Revises: b90304f277d7
Create Date: 2024-01-19 11:10:43.595323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '819665adf2f8'
down_revision = 'b90304f277d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task__template', schema=None) as batch_op:
        batch_op.add_column(sa.Column('notes', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task__template', schema=None) as batch_op:
        batch_op.drop_column('notes')

    # ### end Alembic commands ###