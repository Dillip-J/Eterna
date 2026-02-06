# # #modles/services.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from database import get_db
import models


router = APIRouter(prefix="/services", tags=["Services"])

@router.get("/")
def get_services(db: Session = Depends(get_db)):
    return db.query(models.Service).all()

@router.patch("/{service_id}/price")
def update_service_price(service_id: int, price: float, db: Session = Depends(get_db)):
    service = db.query(models.Service).filter(models.Service.service_id == service_id).first()
    if not service: raise HTTPException(status_code=404)
    service.base_price = price
    db.commit()
    return {"message": "Price updated"}
# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from database import get_db
# import models

# router = APIRouter(prefix="/support", tags=["Support"])

# @router.get("/")
# def get_support(db: Session = Depends(get_db)):
#     # Fetch admins with the 'support' role
#     staff = db.query(models.Admin).filter(models.Admin.role == "support").all()
    
#     return {
#         "header": "Help & Support",
#         "contacts": [
#             {"name": s.name, "email": s.email} 
#             for s in staff
#         ],
#         "faqs": [
#             {"q": "How to cancel a booking?", "a": "Go to the Bookings tab and select Cancel."},
#             {"q": "How to view reports?", "a": "Navigate to the Medical Records section."}
#         ]
#     }
# from fastapi import APIRouter, Depends, Query
# from sqlalchemy.orm import Session
# from database import get_db
# from typing import Optional, List

# # CORRECTED: Import directly from the files to avoid the "models" loop
# from routers.services import Service, ServiceProvider, ProviderService

# router = APIRouter(prefix="/services", tags=["Search Page"])

# @router.get("/")
# def search_services(
#     category: Optional[str] = Query(None),
#     search: Optional[str] = Query(None),
#     db: Session = Depends(get_db)
# ):
#     # Start a base query
#     query = db.query(Service)

#     # Dynamically add filters
#     if category:
#         query = query.filter(Service.category.ilike(f"%{category}%"))
#     if search:
#         query = query.filter(Service.service_name.ilike(f"%{search}%"))

#     return query.all()

# @router.get("/{service_id}/providers")
# def get_providers(service_id: int, db: Session = Depends(get_db)):
#     """List providers offering this specific service."""
#     # We query the bridge table (ProviderService) to get the prices
#     results = db.query(ProviderService).filter(ProviderService.service_id == service_id).all()
    
#     # Format the response to include provider details via relationship
#     return [
#         {
#             "provider_id": item.provider.provider_id,
#             "name": item.provider.name,
#             "provider_type": item.provider.provider_type,
#             "price": item.price,
#             "status": item.status
#         }
#         for item in results
#     ]