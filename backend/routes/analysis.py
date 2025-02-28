from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()
DB_URL = os.getenv("DATABASE_URL", "sqlite:///aahaar_mitra.db")
engine = create_engine(DB_URL)

class MealAnalysisRequest(BaseModel):
    food_name: str

@router.post("/api/nutrition/analyze")
def analyze_meal(request: MealAnalysisRequest):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM recipes WHERE food_name=:food_name"), {"food_name": request.food_name})
            data = [dict(row._mapping) for row in result]
            if not data:
                raise HTTPException(status_code=404, detail="Food not found!")
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))