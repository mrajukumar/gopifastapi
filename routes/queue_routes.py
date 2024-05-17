from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from models.User import Queues
from models.models import QueueCreate, QueueUpdate, QueueOut
from controller import queue_crud

router = APIRouter()

@router.post("/queues/", response_model=QueueOut)
def create_queue(queue_data: QueueCreate, db: Session = Depends(get_db)):
    queue = queue_crud.create_queue(db, **queue_data.dict())
    return queue

@router.get("/queues/{queue_id}", response_model=QueueOut)
def read_queue(queue_id: int, db: Session = Depends(get_db)):
    queue = queue_crud.get_queue(db, queue_id)
    if queue is None:
        raise HTTPException(status_code=404, detail="Queue not found")
    return queue

@router.get("/queues/", response_model=List[QueueOut])
def read_all_queues(db: Session = Depends(get_db)):
    queues = queue_crud.get_all_queues(db)
    return queues

@router.put("/queues/{queue_id}", response_model=QueueOut)
def update_queue(queue_id: int, queue_data: QueueUpdate, db: Session = Depends(get_db)):
    queue = queue_crud.update_queue(db, queue_id, **queue_data.dict())
    if queue is None:
        raise HTTPException(status_code=404, detail="Queue not found")
    return queue

@router.delete("/queues/{queue_id}")
def delete_queue(queue_id: int, db: Session = Depends(get_db)):
    deleted = queue_crud.delete_queue(db, queue_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Queue not found")
    return {"message": "Queue deleted successfully"}
