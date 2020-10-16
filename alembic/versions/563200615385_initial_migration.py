"""initial migration

Revision ID: 563200615385
Revises: b8bbefaf26c2
Create Date: 2020-10-16 10:44:48.969502

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '563200615385'
down_revision = 'b8bbefaf26c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'task_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('task_status', postgresql.ENUM('NOT_STARTED', 'PENDING', 'FINISHED', name='taskstatus'), autoincrement=False, nullable=True))
    # ### end Alembic commands ###