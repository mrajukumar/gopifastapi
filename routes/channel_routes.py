from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.database import get_db
from models.models import ChannelCreate, ChannelUpdate, ChannelsOut
from controller import channel_crud

router = APIRouter()

@router.post("/channels/", response_model=ChannelsOut)
def create_channel(channel_data:ChannelCreate, db: Session = Depends(get_db)):
    channel = channel_crud.create_channel(db, name=channel_data.name)
    return channel

@router.get("/channels/{channel_id}", response_model=ChannelsOut)
def read_channel(channel_id: int, db: Session = Depends(get_db)):
    channel = channel_crud.get_channel(db, channel_id)
    if channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channel

@router.get("/channels/", response_model=List[ChannelsOut])
def read_all_channels(db: Session = Depends(get_db)):
    channels = channel_crud.get_all_channels(db)
    return channels

@router.put("/channels/{channel_id}", response_model=ChannelsOut)
def update_channel(channel_id: int, channel_data: ChannelUpdate, db: Session = Depends(get_db)):
    channel = channel_crud.update_channel(db, channel_id, name=channel_data.name)
    if channel is None:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channel

@router.delete("/channels/{channel_id}")
def delete_channel(channel_id: int, db: Session = Depends(get_db)):
    deleted = channel_crud.delete_channel(db, channel_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Channel not found")
    return {"message": "Channel deleted successfully"}
