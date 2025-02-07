from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def create_app(debug: bool = False):
    app = FastAPI(
        title="Automatics",
        docs_url="/docs",
        debug=debug
    )
    setup_routers(app)
    setup_cors_middleware(app)
    return app


def setup_routers(app: FastAPI) -> None:
    pass
    # app.include_router(, prefix="/api")


def setup_cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        expose_headers=["*"],
        allow_headers=["*"],
    )