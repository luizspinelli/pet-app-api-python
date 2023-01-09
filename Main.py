from decouple import config
from fastapi import FastAPI

from routes.UsersRoute import router as UserRouter

app = FastAPI(
    title="Pet App"
)

app.include_router(UserRouter, tags=['User'], prefix="/api/users")


@app.get("/api/health", tags=["Health"])
async def health():
    return {"result": "ok"}
