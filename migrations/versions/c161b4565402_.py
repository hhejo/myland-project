"""empty message

Revision ID: c161b4565402
Revises: 65c1cb3ae669
Create Date: 2022-02-26 18:42:50.479076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c161b4565402'
down_revision = '65c1cb3ae669'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
