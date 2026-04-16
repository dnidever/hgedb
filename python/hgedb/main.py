from fastapi import FastAPI, HTTPException
import psycopg2

app = FastAPI()

DB_CONN = "dbname=postgres user=postgres password=YOURPASSWORD host=localhost"
SHARED_PASSWORD = "hge-team"

@app.get("/")
def root():
    return {"status": "AS5 HGE API running"}

@app.get("/test_db")
def test_db(password: str):
    if password != SHARED_PASSWORD:
        raise HTTPException(status_code=403, detail="Unauthorized")

    with psycopg2.connect(DB_CONN) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            result = cur.fetchone()

    return {"result": result}
