from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()
DB_URL = os.getenv("DATABASE_URL", "sqlite:///aahaar_mitra.db")
engine = create_engine(DB_URL)

@router.get("/api/fooditems")
def get_fooditems():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM fruits"))
            data = [dict(row._mapping) for row in result]
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/api/mealplan")
def generate_meal_plan(target_calories: int = 2000):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM recipes LIMIT 10"))
            recipes = [dict(row._mapping) for row in result]

        # Just dummy calculation (I'll upgrade this to RDA based later 🔥)
        total_calories = sum(r['energy_kcal'] for r in recipes)
        return {
            "meal_plan": recipes,
            "total_calories": total_calories,
            "target_calories": target_calories
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
