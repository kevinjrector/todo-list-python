import sqlalchemy as sa
from database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String(200), index=True, nullable=False)
    description = sa.Column(sa.Text, index=False)
    completed = sa.Column(sa.Boolean, default=False, index=True, nullable=False)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)
    updated_at = sa.Column(sa.DateTime, server_default=sa.func.now(), nullable=False)
    
    

