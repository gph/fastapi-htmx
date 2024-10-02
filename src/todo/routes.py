""" Todo Router """

from typing import Annotated, Union

from fastapi import APIRouter, Depends, Form, Header, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from src.todo.repository import TodoRepository
from src.todo.schemas import Todo

todo_router = APIRouter()

templates = Jinja2Templates(directory="src/templates")


@todo_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """HomePage"""
    return templates.TemplateResponse(request=request, name="index.html")


@todo_router.get("/todos", response_class=HTMLResponse)
async def list_todos(
    request: Request,
    hx_request: Annotated[Union[str, None], Header()] = None,
    todo_repository: TodoRepository = Depends(TodoRepository),
):
    """List all todos"""

    todos = await todo_repository.get_todos()
    if hx_request:
        return templates.TemplateResponse(
            request=request,
            name="todos.html",
            context={"todos": todos},
        )

    return JSONResponse(content=jsonable_encoder(todos))


@todo_router.post("/todos", response_class=HTMLResponse)
async def create_todo(
    request: Request,
    todo: Annotated[str, Form()],
    todo_repository: TodoRepository = Depends(TodoRepository),
):
    """Create todo from Forms"""
    await todo_repository.create_todo(Todo(todo))
    todos = await todo_repository.get_todos()
    return templates.TemplateResponse(
        request=request, name="todos.html", context={"todos": todos}
    )
