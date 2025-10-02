"""create users table

Revision ID: 593e56d0a667
Revises: 384a5e9156bb
Create Date: 2025-10-02 16:37:31.400354

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '593e56d0a667'
down_revision: Union[str, Sequence[str], None] = '384a5e9156bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
