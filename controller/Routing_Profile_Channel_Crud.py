from sqlalchemy.orm import Session
from models.User import RoutingProfileChannel, RoutingProfile, Channels
from sqlalchemy.orm.exc import NoResultFound

def create_routing_profile_channel(db: Session, routing_profile_id: int, channel_id: int, max_concurrent_interactions: int, cross_channel_concurrency: int):
    try:
        # Query the RoutingProfile table to get the routing_profile
        routing_profile = db.query(RoutingProfile).filter(RoutingProfile.routing_profile_id == routing_profile_id).first()
        if not routing_profile:
            raise ValueError("Routing profile not found")   

        # Query the Channels table to get the channel
        channel = db.query(Channels).filter(Channels.channel_id == channel_id).first()
        if not channel:
            raise ValueError("Channel not found")    

        # Create the RoutingProfileChannel record
        routing_profile_channel = RoutingProfileChannel(
            routing_profile_id=routing_profile_id,
            channel_id=channel_id,
            max_concurrent_interactions=max_concurrent_interactions,
            cross_channel_concurrency=cross_channel_concurrency
        )

        db.add(routing_profile_channel)
        db.commit()
        db.refresh(routing_profile_channel)
        return routing_profile_channel
    except NoResultFound:
        # Rollback transaction in case of error
        db.rollback()
        # Raise an appropriate exception with a meaningful error message
        raise ValueError("Routing profile or channel not found")
    except Exception as e:
        # Rollback transaction in case of error
        db.rollback()
        # Raise an appropriate exception with a meaningful error message
        raise ValueError(f"Failed to create routing profile channel: {str(e)}")






def get_all_routing_profile_channels(db: Session):
    return db.query(RoutingProfileChannel).all()



def get_routing_profile_channel(db: Session, routing_profile_id: int, channel_id: int):
    # Query the RoutingProfileChannel table to find the record with the provided routing_profile_id and channel_id
    return db.query(RoutingProfileChannel).filter(
        RoutingProfileChannel.routing_profile_id == routing_profile_id,
        RoutingProfileChannel.channel_id == channel_id
    ).first()
    return routing_profile_channel

def update_routing_profile_channel(db: Session, routing_profile_id: int, channel_id: int, max_concurrent_interactions: int, cross_channel_concurrency: int):
    routing_profile_channel = get_routing_profile_channel(db, routing_profile_id, channel_id)
    if routing_profile_channel:
        routing_profile_channel.max_concurrent_interactions = max_concurrent_interactions
        routing_profile_channel.cross_channel_concurrency = cross_channel_concurrency
        db.commit()
    return routing_profile_channel

def delete_routing_profile_channel(db: Session, routing_profile_id: int, channel_id: int):
    routing_profile_channel = get_routing_profile_channel(db, routing_profile_id, channel_id)
    if routing_profile_channel:
        db.delete(routing_profile_channel)
        db.commit()
        return True
    return False

