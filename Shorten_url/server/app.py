from fastapi import FastAPI

from server.routes.Url_shorten import router as UrlRouter

app = FastAPI()

app.include_router(UrlRouter, tags=["Url"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
