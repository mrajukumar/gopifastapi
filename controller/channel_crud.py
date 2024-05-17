from sqlalchemy.orm import Session
from models.User import Channels


def create_channel(db: Session, name: str):
    channel = Channels(name=name)
    db.add(channel)
    db.commit()
    db.refresh(channel)
    return channel


def get_channel(db: Session, channel_id: int):
    return db.query(Channels).filter(Channels.channel_id == channel_id).first()


def get_all_channels(db: Session):
    return db.query(Channels).all()


def update_channel(db: Session, channel_id: int, name: str):
    channel = get_channel(db, channel_id)
    if channel:
        channel.name = name
        db.commit()
        db.refresh(channel)
    return channel


def delete_channel(db: Session, channel_id: int):
    channel = get_channel(db, channel_id)
    if channel:
        db.delete(channel)
        db.commit()
        return True
    return False
