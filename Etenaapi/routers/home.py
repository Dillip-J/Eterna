# # routers/home.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from database import get_db
import models
from datetime import datetime

router = APIRouter(prefix="/home", tags=["User Home"])

@router.get("/")
def get_user_home(user_id: int = None, db: Session = Depends(get_db)):
    # 1. Categories
    categories = db.query(models.Service.category).distinct().all()
    
    # 2. Featured Services
    featured = db.query(models.Service).limit(5).all()

    # 3. Active Booking Banner (Only if logged in)
    active = None
    if user_id:
        active_booking = db.query(models.Booking).options(joinedload(models.Booking.service))\
            .filter(models.Booking.user_id == user_id, 
                    models.Booking.booking_status == 'confirmed',
                    models.Booking.scheduled_time > datetime.now())\
            .order_by(models.Booking.scheduled_time.asc()).first()
        
        if active_booking:
            active = {
                "booking_id": active_booking.booking_id,
                "service_name": active_booking.service.service_name,
                "time": active_booking.scheduled_time
            }

    return {
        "categories": [c[0] for c in categories if c[0]],
        "featured": featured,
        "active_booking": active
    }
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session, joinedload
# from database import get_db
# import models
# from typing import Optional
# from datetime import datetime

# router = APIRouter(prefix="/home", tags=["User Home"])

# @router.get("/")
# def get_user_home(user_id: Optional[int] = None, db: Session = Depends(get_db)):
#     response = {"categories": [], "featured": [], "active_booking": None}

#     # 1. Fetch Categories (using entities for performance)
#     categories = db.query(models.Service.category).distinct().all()
#     response["categories"] = [cat[0] for cat in categories if cat[0]]

#     # 2. Featured Services (limiting to 5 for a clean UI)
#     featured = db.query(models.Service).limit(5).all()
#     response["featured"] = featured

#     # 3. Personalized Active Booking Banner
#     if user_id:
#         # We use joinedload to fetch Service details in the SAME query
#         active = db.query(models.Booking)\
#             .options(joinedload(models.Booking.service))\
#             .filter(
#                 models.Booking.user_id == user_id,
#                 models.Booking.booking_status == 'confirmed',
#                 models.Booking.scheduled_time > datetime.now()
#             )\
#             .order_by(models.Booking.scheduled_time.asc())\
#             .first()

#         if active:
#             response["active_booking"] = {
#                 "booking_id": active.booking_id,
#                 "service_name": active.service.service_name, # Fast access!
#                 "scheduled_time": active.scheduled_time,
#                 "provider_name": active.provider.name if active.provider else None
#             }

#     return response