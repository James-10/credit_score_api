import os

class Config:
    CREDIT_MODEL_NAME: str = "Basic Credit Score Model"
    CREDIT_MODEL_VERSION: str = "1.0.0"
    
    # MongoDB configurations
    MONGO_USERNAME: str = os.getenv("MONGO_USERNAME")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD")
    MONGO_HOST: str = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT: int = int(os.getenv("MONGO_PORT", "27017"))
    MONGO_URI: str = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
    MONGO_DB_NAME: str = "credit_score_db"
    MONGO_COLLECTION_NAME: str = "credit_score_requests"

