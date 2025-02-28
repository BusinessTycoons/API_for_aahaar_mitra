from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import meal_plan, analysis, auth

app = FastAPI()

# Include Routers
app.include_router(meal_plan.router)
app.include_router(analysis.router)
app.include_router(auth.router)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {"message": "Aahaar Mitra API is running"}