from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # ============ APP ============
    APP_NAME: str = "Redline Academy LMS"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True
    APP_URL: str = "http://localhost:8000"
    FRONTEND_URL: str = "http://localhost:5173"

    # ============ SUPABASE ============
    SUPABASE_URL: str = ""
    SUPABASE_ANON_KEY: str = ""
    SUPABASE_SERVICE_ROLE_KEY: str = ""
    SUPABASE_JWT_SECRET: str = ""

    # ============ DATABASE ============
    DATABASE_URL: str = ""

    # ============ JWT ============
    JWT_SECRET: str = "change_me_to_random_32_char_string_now"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRES_MINUTES: int = 60

    # ============ CORS ============
    CORS_ORIGINS: str = "http://localhost:5173"

    # ============ EMAIL ============
    RESEND_API_KEY: str = ""
    MAIL_FROM: str = "noreply@redline.id"
    MAIL_FROM_NAME: str = "Redline Academy"

    # ============ PAYMENT ============
    MIDTRANS_SERVER_KEY: str = ""
    MIDTRANS_CLIENT_KEY: str = ""
    MIDTRANS_IS_PRODUCTION: bool = False

    # ============ REDIS ============
    REDIS_URL: str = "redis://localhost:6379/0"

    # ============ SENTRY ============
    SENTRY_DSN: str = ""

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]

    @property
    def is_production(self) -> bool:
        return self.APP_ENV == "production"

    @property
    def is_development(self) -> bool:
        return self.APP_ENV == "development"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
