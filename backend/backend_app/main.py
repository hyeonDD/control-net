import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend_app.api.router import api_router
from backend_app.core.config import settings

app = FastAPI(openapi_url=f'{
              settings.PREFIX_URL}/openapi.json', docs_url=f'{settings.PREFIX_URL}/docs')
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(f"{settings.PREFIX_URL}/")
async def root():
    return {"message": "This is ControlNet server!!"}


def start():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


app.include_router(api_router, prefix=settings.PREFIX_URL)

if __name__ == "__main__":
    start()
