from fastapi import APIRouter

from app.core.config import settings
from app.core.supabase import get_supabase_admin

router = APIRouter()


@router.get("")
async def health_check():
    db_status = "not_configured"
    roles_count = 0

    if settings.SUPABASE_URL and settings.SUPABASE_SERVICE_ROLE_KEY:
        try:
            client = get_supabase_admin()
            result = client.table("roles").select("name").execute()
            roles_count = len(result.data)
            db_status = "connected"
        except Exception as e:
            db_status = f"error: {str(e)[:100]}"

    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "env": settings.APP_ENV,
        "database": db_status,
        "roles_seeded": roles_count,
    }


@router.get("/ping")
async def ping():
    return {"pong": True}
