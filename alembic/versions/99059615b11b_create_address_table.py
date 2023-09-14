"""Create address table

Revision ID: 99059615b11b
Revises: f116584e3577
Create Date: 2023-09-14 15:51:25.052708

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99059615b11b'
down_revision: Union[str, None] = 'f116584e3577'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
