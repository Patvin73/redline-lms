from functools import lru_cache
from supabase import create_client, Client

from app.core.config import settings


@lru_cache
def get_supabase_admin() -> Client:
    """Service role client — BYPASS RLS, untuk backend logic.

    Lazy load: hanya connect saat pertama kali dipanggil, bukan saat import.
    """
    if not settings.SUPABASE_URL or not settings.SUPABASE_SERVICE_ROLE_KEY:
        raise RuntimeError(
            "SUPABASE_URL dan SUPABASE_SERVICE_ROLE_KEY belum di-set di .env. "
            "Isi dulu sebelum menggunakan fitur Supabase."
        )
    return create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_SERVICE_ROLE_KEY,
    )


@lru_cache
def get_supabase_anon() -> Client:
    """Anon client — respect RLS, untuk operasi user-context."""
    if not settings.SUPABASE_URL or not settings.SUPABASE_ANON_KEY:
        raise RuntimeError("SUPABASE_URL dan SUPABASE_ANON_KEY belum di-set di .env.")
    return create_client(
        settings.SUPABASE_URL,
        settings.SUPABASE_ANON_KEY,
    )
