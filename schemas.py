from pydantic import BaseModel, Field
from datetime import datetime

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="The title of the task")
    description: str | None = Field(None, description="The detailed description of the task")
    due_date: datetime | None = Field(None, description="The due date of the task")
    
class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200, description="The title of the task")
    description: str | None = Field(None, description="The detailed description of the task")
    due_date: datetime | None = Field(None, description="The due date of the task")
    completed: bool | None = Field(None, description="Completion status of the task")
    
class TaskResponse(TaskBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True