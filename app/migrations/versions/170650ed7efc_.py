"""empty message

Revision ID: 170650ed7efc
Revises: 69f0392ecc03
Create Date: 2017-06-16 07:55:48.504407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '170650ed7efc'
down_revision = '69f0392ecc03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('UC_Vendor_Person_ids', 'vendor_contact_association', ['Vendor_Shortcut', 'Person_Oid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('UC_Vendor_Person_ids', 'vendor_contact_association', type_='unique')
    # ### end Alembic commands ###
