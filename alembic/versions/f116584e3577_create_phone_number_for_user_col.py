"""create phone number for user col

Revision ID: f116584e3577
Revises: 
Create Date: 2023-09-14 15:28:36.840072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f116584e3577'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.Integer(), nullable=True))


def downgrade() -> None:
    pass
