from sqlalchemy.orm import Session
from models.User import Queues

def create_queue(db: Session, name: str, wrapup_time: int = None):
    queue = Queues(name=name, wrapup_time=wrapup_time)
    db.add(queue)
    db.commit()
    db.refresh(queue)
    return queue

def get_queue(db: Session, queue_id: int):
    return db.query(Queues).filter(Queues.queue_id == queue_id).first()

def get_all_queues(db: Session):
    return db.query(Queues).all()

def update_queue(db: Session, queue_id: int, name: str, wrapup_time: int = None):
    queue = db.query(Queues).filter(Queues.queue_id == queue_id).first()
    if queue:
        queue.name = name
        queue.wrapup_time = wrapup_time
        db.commit()
        db.refresh(queue)
    return queue

def delete_queue(db: Session, queue_id: int):
    queue = db.query(Queues).filter(Queues.queue_id == queue_id).first()
    if queue:
        db.delete(queue)
        db.commit()
        return True
    return False
