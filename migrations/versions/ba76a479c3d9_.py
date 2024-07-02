"""empty message

Revision ID: ba76a479c3d9
Revises: 7e6bfdca19a1
Create Date: 2024-07-02 00:32:23.997836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba76a479c3d9'
down_revision = '7e6bfdca19a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shoe_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.String(length=120), nullable=False),
    sa.Column('total_price', sa.String(length=120), nullable=False),
    sa.Column('order_date', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['shoe_id'], ['shoes_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders_table')
    # ### end Alembic commands ###
