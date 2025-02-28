from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DB_URL = os.getenv('DATABASE_URL', 'sqlite:///aahaar_mitra.db')
engine = create_engine(DB_URL)

def calculate_rda(age, gender, activity_level):
    try:
        with engine.connect() as conn:
            # Query the RDA table for the specific age, gender, and activity level
            query = text("""
                SELECT calories, protein, carbohydrates, fats
                FROM rda_targets
                WHERE age = :age AND gender = :gender AND activity_level = :activity_level
            """)
            result = conn.execute(query, {"age": age, "gender": gender, "activity_level": activity_level})
            rda_values = result.fetchone()

            if rda_values:
                return dict(rda_values)
            else:
                return {"error": "RDA values not found for the specified criteria."}

    except Exception as e:
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    age = 25
    gender = "male"
    activity_level = "moderate"
    rda = calculate_rda(age, gender, activity_level)
    print(f"RDA for a {age}-year-old {gender} with {activity_level} activity level: {rda}")