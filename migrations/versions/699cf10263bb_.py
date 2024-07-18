"""empty message

Revision ID: 699cf10263bb
Revises: 
Create Date: 2024-07-13 23:52:07.074990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '699cf10263bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('full_name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('full_name')
    )
    op.create_table('feedback_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shipping_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shipping_address', sa.String(length=120), nullable=False),
    sa.Column('billing_address', sa.String(length=120), nullable=False),
    sa.Column('credit_card_num', sa.String(length=16), nullable=False),
    sa.Column('credit_card_cvv', sa.String(length=3), nullable=False),
    sa.Column('credit_card_year', sa.String(length=120), nullable=False),
    sa.Column('credit_card_month', sa.String(length=120), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_table.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('billing_address'),
    sa.UniqueConstraint('credit_card_cvv'),
    sa.UniqueConstraint('credit_card_month'),
    sa.UniqueConstraint('credit_card_num'),
    sa.UniqueConstraint('credit_card_year'),
    sa.UniqueConstraint('shipping_address')
    )
    op.create_table('shoes_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shoe_name', sa.String(length=120), nullable=False),
    sa.Column('shoe_size', sa.String(length=120), nullable=False),
    sa.Column('manufacturer', sa.String(length=120), nullable=False),
    sa.Column('shoe_price', sa.String(length=120), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('shoe_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['shoe_id'], ['shoes_table.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.drop_table('favorites_table')
    op.drop_table('shoes_table')
    op.drop_table('shipping_table')
    op.drop_table('feedback_table')
    op.drop_table('user_table')
    # ### end Alembic commands ###
