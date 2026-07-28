from fastapi import FastAPI
from app.routes.requests import router as requests_router
from app.routes.service_requests import router as service_requests_router


app = FastAPI(
    title="Cloud AI Assistant",
    version="1.0.0"
)

@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "cloud-provisioning-ai-assistant",
    }


app.include_router(requests_router)
app.include_router(service_requests_router)