from fastapi import FastAPI #pip install fastapi uvicorn sqlalchemy pymysql
                            #uvicorn main:app --reload  it use to start server
app = FastAPI()

@app.get("/")
def home():
    return {"RS"}