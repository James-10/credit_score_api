from fastapi import FastAPI
from pydantic import BaseModel
from scorecard.model import calculate_credit_score
from config import Config
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import uvicorn

app = FastAPI()

class CreditScoreRequest(BaseModel):
    payment_history: float
    credit_utilization: float
    credit_history_length: int
    credit_mix: int
    recent_inquiries: int
    total_debt: float
    income: float
    employment_status: bool
    age: int

# MongoDB client
mongo_client = AsyncIOMotorClient(Config.MONGO_URI)
db = mongo_client[Config.MONGO_DB_NAME]
collection = db[Config.MONGO_COLLECTION_NAME]

@app.get("/")
async def root():
    return {"message": "Welcome to the Credit Score API"}

@app.post("/credit_score")
async def calculate_score(request: CreditScoreRequest):
    """
    Calculate a credit score based on the provided request data.

    Args:
        request (CreditScoreRequest): The input data containing various financial and personal factors.

    Returns:
        dict: A dictionary containing the calculated credit score, model name, and model version.
    """
    input_data = request.model_dump()

    score = calculate_credit_score(**input_data)
    
    # Prepare data for MongoDB
    mongo_data = {
        **input_data,
        "credit_score": score,
        "timestamp": datetime.now().astimezone(),
        "model_name": Config.CREDIT_MODEL_NAME,
        "model_version": Config.CREDIT_MODEL_VERSION
    }
    
    # Write to MongoDB
    await collection.insert_one(mongo_data)
    
    return {
        "credit_score": score,
        "model_name": Config.CREDIT_MODEL_NAME,
        "model_version": Config.CREDIT_MODEL_VERSION
    }

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(Config.MONGO_URI)
    app.mongodb = app.mongodb_client[Config.MONGO_DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)