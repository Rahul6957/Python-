from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/student_management"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

try:
    connection = engine.connect()

    print("Database connected successfully!")

    connection.close()

except Exception as e:
    print("Database connection failed!")
    print(e)