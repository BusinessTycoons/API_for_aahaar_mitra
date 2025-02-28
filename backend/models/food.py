from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    calories = Column(Float)
    protein = Column(Float)
    carbohydrates = Column(Float)
    fats = Column(Float)

    def __repr__(self):
        return f"<Food(name={self.name}, calories={self.calories})>"