from fastapi import FastAPI
from decouple import config

app = FastAPI()


@app.get("/api/health", tags=["Health"])
async def health():
    DB_PASSWORD = config('DB_PASSWORD')
    return {"status": DB_PASSWORD}
