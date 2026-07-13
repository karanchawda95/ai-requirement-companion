from datetime import datetime, UTC
from typing import Any
from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

@router.get("", summary="Health Check", description="Check the health status of the service.")
def health_check() -> dict[str, Any]:
    return {"status": "healthy",
            "timestamp": datetime.now(UTC),
            "version": "0.1.0"}