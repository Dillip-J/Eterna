# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models
from routers import auth, booking, home, records, support, services
# Initialize Database Tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="V Healthcare API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH"],
    allow_headers=["*"],
)

# Connect Routers
app.include_router(auth.router)
app.include_router(home.router)
app.include_router(services.router)
app.include_router(booking.router)
app.include_router(records.router)
app.include_router(support.router)

@app.get("/")
def root():
    return {"status": "V Healthcare API is Online"}
# import logging
# from contextlib import asynccontextmanager
# from fastapi import FastAPI
# from models import user
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn

# # 1. Import Database Engine and Base
# from database import engine, Base
# import models  # This ensures all models are loaded before table creation

# # 2. Import actual Healthcare routers
# from models import services
# from routers import (
#     auth,
#     booking,
#     home, 
#     records, 
#     support, 
#     websockets
# )

# # Logging Configuration
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Lifespan (Startup & Shutdown)
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # --- Startup ---
#     logger.info("🚀 Starting V (Vision) Healthcare API...")
    
#     try:
#         # 3. Create Tables automatically if they don't exist
#         logger.info("🛠️ Creating/Updating Database Tables...")
#         Base.metadata.create_all(bind=engine)
#         logger.info("✅ Database initialized successfully")
#     except Exception as e:
#         logger.error(f"❌ Database initialization failed: {e}")

#     yield  # Application runs here

#     # --- Shutdown ---
#     logger.info("🛑 Shutting down V (Vision) Healthcare API")

# # App Initialization
# app = FastAPI(
#     title="V (Vision) Healthcare API",
#     description="Convenient and Time-Efficient Healthcare",
#     version="1.0.0",
#     lifespan=lifespan
# )

# # CORS Middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Routers Registration
# app.include_router(auth.router)
# app.include_router(home.router)
# app.include_router(services.router)
# app.include_router(booking.router)
# app.include_router(records.router)
# app.include_router(support.router)
# app.include_router(websockets.router)

# @app.get("/")
# def root():
#     return {
#         "message": "V (Vision) Healthcare API is running",
#         "status": "healthy",
#         "orm": "SQLAlchemy Enabled"
#     }

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)