#models
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, DateTime, Text, Numeric
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String)
    bookings = relationship("Booking", back_populates="user")

class Service(Base):
    __tablename__ = "services"
    service_id = Column(BigInteger, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    category = Column(String)
    base_price = Column(Numeric(10, 2))

class ServiceProvider(Base):
    __tablename__ = "service_providers"
    provider_id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    provider_type = Column(String)

class ProviderService(Base):
    __tablename__ = "provider_services"
    provider_id = Column(BigInteger, ForeignKey("service_providers.provider_id"), primary_key=True)
    service_id = Column(BigInteger, ForeignKey("services.service_id"), primary_key=True)
    price = Column(Numeric(10, 2))
    status = Column(String)
    provider = relationship("ServiceProvider")

class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    provider_id = Column(BigInteger, ForeignKey("service_providers.provider_id"))
    service_id = Column(BigInteger, ForeignKey("services.service_id"))
    scheduled_time = Column(DateTime, nullable=False)
    booking_status = Column(String, default="pending")
    
    user = relationship("User", back_populates="bookings")
    service = relationship("Service")
    provider = relationship("ServiceProvider")

class MedicalRecord(Base):
    __tablename__ = "medical_records"
    record_id = Column(BigInteger, primary_key=True)
    booking_id = Column(BigInteger, ForeignKey("bookings.booking_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"))
    provider_id = Column(BigInteger, ForeignKey("service_providers.provider_id"))
    diagnosis = Column(Text)
    report_url = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    booking = relationship("Booking")
    provider = relationship("ServiceProvider")

class Admin(Base):
    __tablename__ = "admins"
    admin_id = Column(BigInteger, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)