
from fastapi import FastAPI

from src.auth.routers import router as users_router
from config import settings
from db.database import User, db
app = FastAPI(
    title=settings.PROJECT_NAME,
)


app.include_router(users_router)

if __name__ == "__main__":
    import uvicorn
    from beanie import init_beanie


    @app.on_event("startup")
    async def on_startup():
        await init_beanie(
            database=db,
            document_models=[
                User,
            ],
        )


    uvicorn.run(app, host="0.0.0.0", port=8000)
