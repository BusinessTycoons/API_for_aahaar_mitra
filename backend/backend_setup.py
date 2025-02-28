import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

DB_URL = os.getenv('DATABASE_URL', 'sqlite:///aahaar_mitra.db')  # Use env variable if available
EXCEL_FILE = os.getenv('EXCEL_FILE', 'Food database and RDA values combined.xlsx')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create DB Engine
def get_db_engine():
    try:
        engine = create_engine(DB_URL, echo=True)
        return engine
    except Exception as e:
        logging.error(f"Error creating database engine: {e}")
        raise

# Automatic Seeder Function
def seed_database():
    try:
        engine = get_db_engine()
        xls = pd.ExcelFile(EXCEL_FILE)
        
        for sheet in xls.sheet_names:
            df = pd.read_excel(EXCEL_FILE, sheet_name=sheet)
            table_name = sheet.lower().replace(" ", "_")
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)
            logging.info(f"✅ Table {table_name} Seeded")
    except Exception as e:
        logging.error(f"Error seeding database: {e}")
        raise

if __name__ == '__main__':
    logging.info("Seeding Database... 🔥")
    seed_database()
    logging.info("✅ Database Seeding Complete!")