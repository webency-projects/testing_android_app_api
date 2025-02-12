from fastapi import FastAPI
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.core.logger import Logger
from app.domain.device.api import device_api
from app.domain.notification.api import notification_api
from app.domain.user.api import user_api

log = Logger.get_logger(__name__)


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except HTTPException as http_exception:
            return JSONResponse(
                status_code=http_exception.status_code,
                content={"error": "Client Error", "message": str(http_exception.detail)},
            )
        except Exception as e:
            log.exception(msg=e.__class__.__name__, args=e.args)
            return JSONResponse(
                status_code=500,
                content={"error": "Internal Server Error", "message": "An unexpected error occurred."},
            )


def create_app(debug: bool = False):
    app = FastAPI(
        title="Automatics",
        docs_url="/docs",
        debug=debug
    )
    setup_routers(app)
    setup_cors_middleware(app)
    app.add_middleware(ExceptionHandlerMiddleware)
    return app


def setup_routers(app: FastAPI) -> None:
    app.include_router(device_api, prefix="/api")
    app.include_router(user_api, prefix="/api")
    app.include_router(notification_api, prefix="/api")


def setup_cors_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        expose_headers=["*"],
        allow_headers=["*"],
    )
