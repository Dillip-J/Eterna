# # schemas.py
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from datetime import datetime
from decimal import Decimal

# Helper to allow Pydantic to read SQLAlchemy objects
class ORMBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

# --- Auth ---
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# --- Bookings ---
class BookingCreate(BaseModel):
    user_id: int
    provider_id: int
    service_id: int
    scheduled_time: datetime

# --- Responses ---
class ServiceResponse(ORMBase):
    service_id: int
    service_name: str
    category: str
    base_price: Decimal
# from pydantic import BaseModel, EmailStr, ConfigDict
# from typing import Optional, List
# from datetime import datetime
# from decimal import Decimal

# # --- Base Schema with ORM Config ---
# class ORMBase(BaseModel):
#     model_config = ConfigDict(from_attributes=True)

# # --- User Auth ---
# class UserCreate(BaseModel):
#     name: str
#     email: EmailStr
#     password: str
#     phone: Optional[str] = None

# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str

# class UserResponse(ORMBase):
#     user_id: int
#     name: str
#     email: str
#     phone: Optional[str]

# # --- Booking ---
# class BookingCreate(BaseModel):
#     user_id: int
#     provider_id: int
#     service_id: int
#     scheduled_time: datetime

# class BookingResponse(ORMBase):
#     booking_id: int
#     scheduled_time: datetime
#     booking_status: str
#     # We can include nested data from relationships here
#     service_name: Optional[str] = None 
#     provider_name: Optional[str] = None

# # --- Feedback ---
# class ReviewCreate(BaseModel):
#     booking_id: int
#     rating: int
#     comment: Optional[str] = None

# class ComplaintCreate(BaseModel):
#     booking_id: int
#     user_id: int
#     provider_id: int
#     complaint_text: str

# # --- Home & Search (New) ---
# class ServiceResponse(ORMBase):
#     service_id: int
#     service_name: str
#     category: str
#     base_price: Decimal

# class HomePageResponse(BaseModel):
#     categories: List[str]
#     featured: List[ServiceResponse]
#     active_booking: Optional[BookingResponse] = None