from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from typing import List
from models.User import RoutingProfileChannel 
from models.models import RoutingProfileChannelCreate, RoutingProfileChannelResponseBody, RoutingProfileChannelResponse  # Import the model

from controller import Routing_Profile_Channel_Crud

router = APIRouter()

@router.post("/routing_profile_channel/", response_model=RoutingProfileChannelResponse)
def create_routing_profile_channel(routing_profile_channel_request: RoutingProfileChannelCreate, db: Session = Depends(get_db)):  
    try:
        # Create a new RoutingProfileChannel instance
        routing_profile_channel = Routing_Profile_Channel_Crud.create_routing_profile_channel(
            db, 
            routing_profile_id=routing_profile_channel_request.routing_profile_id, 
            channel_id=routing_profile_channel_request.channel_id, 
            max_concurrent_interactions=routing_profile_channel_request.max_concurrent_interactions, 
            cross_channel_concurrency=routing_profile_channel_request.cross_channel_concurrency
        )

        # Return the created routing_profile_channel as response
        return routing_profile_channel
    except Exception as e:
        # Handle the exception
        raise HTTPException(status_code=500, detail=f"Failed to create routing profile channel: {str(e)}")




@router.get("/routing_profile_channel/{routing_profile_id}/{channel_id}", response_model=RoutingProfileChannelResponseBody)
def get_routing_profile_channel(routing_profile_id: int, channel_id: int, db: Session = Depends(get_db)):
    routing_profile_channel = Routing_Profile_Channel_Crud.get_routing_profile_channel(db, routing_profile_id, channel_id)
    if routing_profile_channel is None:
        raise HTTPException(status_code=404, detail="Routing profile channel not found")

    return routing_profile_channel

# @router.get("/routing_profile_channel/{routing_profile_id}/{channel_id}", response_model=RoutingProfileChannelResponseBody)
# def get_routing_profile_channel(routing_profile_id: int, channel_id: int, db: Session = Depends(get_db)):
#     routing_profile_channel = db.query(RoutingProfileChannel).filter(RoutingProfileChannel.routing_profile_id == routing_profile_id, RoutingProfileChannel.channel_id == channel_id).first()
#     if routing_profile_channel is None:
#         raise HTTPException(status_code=404, detail="Routing profile channel not found")
    
#     # Map the attributes to RoutingProfileChannelResponseBody
#     return RoutingProfileChannelResponseBody(
#         routing_profile_id=routing_profile_channel.routing_profile_id,
#         channel_id=routing_profile_channel.channel_id,
#         max_concurrent_interactions=routing_profile_channel.max_concurrent_interactions,
#         cross_channel_concurrency=routing_profile_channel.cross_channel_concurrency
#     )



@router.put("/routing_profile_channel/{routing_profile_id}/{channel_id}", response_model=RoutingProfileChannelResponseBody)
def update_routing_profile_channel(routing_profile_id: int, channel_id: int, max_concurrent_interactions: int, cross_channel_concurrency: int, db: Session = Depends(get_db)):
    routing_profile_channel = db.query(RoutingProfileChannel).filter(RoutingProfileChannel.routing_profile_id == routing_profile_id, RoutingProfileChannel.channel_id == channel_id).first()
    if routing_profile_channel is None:
        raise HTTPException(status_code=404, detail="Routing profile channel not found")
    routing_profile_channel.max_concurrent_interactions = max_concurrent_interactions
    routing_profile_channel.cross_channel_concurrency = cross_channel_concurrency
    db.commit()
    return routing_profile_channel

# Delete
@router.delete("/routing_profile_channel/{routing_profile_id}/{channel_id}")
def delete_routing_profile_channel(routing_profile_id: int, channel_id: int, db: Session = Depends(get_db)):
    routing_profile_channel = db.query(RoutingProfileChannel).filter(RoutingProfileChannel.routing_profile_id == routing_profile_id, RoutingProfileChannel.channel_id == channel_id).first()
    if routing_profile_channel is None:
        raise HTTPException(status_code=404, detail="Routing profile channel not found")
    db.delete(routing_profile_channel)
    db.commit()
    return {"message": "Routing profile channel deleted successfully"}

# Get all
@router.get("/routing_profile_channels/", response_model=List[RoutingProfileChannelResponseBody])
def get_all_routing_profile_channels(db: Session = Depends(get_db)):
    return db.query(RoutingProfileChannel).all()
