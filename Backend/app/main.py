from fastapi import FastAPI
from .database import db
# from routes.user_routes import router as user_router

app = FastAPI(
    title="Aptech Freelancing Platform",
    version="1.0.0",
    description="Backend API for student and company users"
)

# Test root route
@app.get("/")
def root():
    return {"message": "API is working 🚀"}

# Test MongoDB connection
@app.get("/test-db")
async def test_db():
    try:
        await db.command("ping")
        return {"message": "MongoDB connected successfully ✅"}
    except Exception as e:
        return {"error": str(e)}

# Register all routers
# app.include_router(user_router, prefix="/users", tags=["Users"])
