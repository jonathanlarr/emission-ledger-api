from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.authorizations.router import router as authorizations_router


DESCRIPTION = """
This API is an example of how to implement Dock External Authorization Service.
The service it is called by Dock API to authorize the requests of
a card transaction, .e.g. purchase, consult balance, etc.
"""


app = FastAPI(
    title=settings.api_name,
    description=DESCRIPTION,
    version=settings.api_version,
)

origins = [
    "http://localhost:8000",
    "http://localhost",
    "https://tudominio.com", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health check"])
async def health_check():
    """
    Health Check Endpoint
    ---
    Description: This endpoint is used to check the health of the service.
    """
    return {"status": "ok"}


# Include routers
app.include_router(authorizations_router, prefix="/api/v1")


