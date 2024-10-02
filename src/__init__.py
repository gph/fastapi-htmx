""" FastAPI app instance """

from fastapi import FastAPI

from src.todo.routes import todo_router

VERSION = "v1"
DESCRIPTION = "Learning about FastAPI + HTMX"
version_prefix = f"/api/{VERSION}"


app = FastAPI(
    title="FastAPI + HTMX",
    description=DESCRIPTION,
    version=VERSION,
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "url": "https://github.com/gph",
    },
    openapi_url=f"{version_prefix}/openapi.json",
    docs_url=f"{version_prefix}/docs",
    redoc_url=f"{version_prefix}/redoc",
)

app.include_router(todo_router)
