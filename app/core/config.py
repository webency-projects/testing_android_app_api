import os


class Settings:
    PROJECT_NAME: str = 'Project X'

    # jwt
    JWT_ALGORITHM: str = "HS256"
    JWT_SECRET_KEY: str = ""
    JWT_ACCESS_EXPIRE_MINUTES: int = 15
    JWT_REFRESH_EXPIRE_MINUTES: int = 600

    # databases
    PG_DB_USER: str = os.getenv("PG_DB_USER", "postgres")
    PG_DB_PASSWORD: str = os.getenv("PG_DB_PASSWORD", "postgres")
    PG_DB_HOST: str = os.getenv("PG_DB_HOST", "localhost")
    PG_DB_PORT: int = 5432
    PG_DB_NAME: str = "project_db"

    DATABASE_URL = f"postgresql+asyncpg://{PG_DB_USER}:{PG_DB_PASSWORD}@{PG_DB_HOST}:{PG_DB_PORT}/{PG_DB_NAME}"


settings = Settings()
