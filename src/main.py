import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import settings
from redis import asyncio as aioredis
from router.router import router


app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS}", encoding="utf8", decode_responses=False)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


if __name__ == "__main__":
    uvicorn.run(app=app, host=settings.HOST, port=settings.PORT)
