from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db, Base
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse

app = FastAPI(
    title="To-Do List API",
    description="A simple API for managing a to-do list",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

@app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)

def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    
    db_task = Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
    )
    
    db.add(db_task)
    
    db.commit()
    
    db.refresh(db_task)
    
    return db_task

@app.get("/tasks/", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    
    tasks = db.query(Task).all()
    
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    return task