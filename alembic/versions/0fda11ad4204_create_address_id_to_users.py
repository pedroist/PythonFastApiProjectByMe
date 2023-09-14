"""create address_id to users

Revision ID: 0fda11ad4204
Revises: 99059615b11b
Create Date: 2023-09-14 16:00:31.455231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fda11ad4204'
down_revision: Union[str, None] = '99059615b11b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
