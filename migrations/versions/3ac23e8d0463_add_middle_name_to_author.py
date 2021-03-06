"""add middle_name to Author

Revision ID: 3ac23e8d0463
Revises: 56cb43788bae
Create Date: 2021-08-22 05:55:23.428120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ac23e8d0463'
down_revision = '56cb43788bae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author_model', sa.Column('middle_name', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('author_model', 'middle_name')
    # ### end Alembic commands ###
