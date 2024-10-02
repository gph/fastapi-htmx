""" Todo Router """

from typing import Annotated, Union

from fastapi import APIRouter, Depends, Form, Header, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.todo.schemas import TodoDTO
from src.todo.service import TodoService

templates = Jinja2Templates(directory="src/templates")

todo_router = APIRouter()


@todo_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """HomePage"""
    return templates.TemplateResponse(request=request, name="index.html")


@todo_router.get("/todos", response_class=HTMLResponse)
async def list_todos(
    request: Request,
    hx_request: Annotated[Union[str, None], Header()] = None,
    todo_service: TodoService = Depends(),
):
    """List all todos"""

    todos = await todo_service.get_todos()
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
    todo_service: TodoService = Depends(),
):
    """Create todo from Forms"""
    todo = TodoDTO(text=todo)
    await todo_service.create_todo(todo)

    # redirect or something...
    todos = await todo_service.get_todos()
    return templates.TemplateResponse(
        request=request, name="todos.html", context={"todos": todos}
    )


@todo_router.put("/todos/{todo_id}", response_class=HTMLResponse)
async def update_todo(
    todo_id: str,
    text: Annotated[str, Form()],
    todo_service: TodoService = Depends(TodoService),
):
    """Update todos"""

    todo_dto = TodoDTO(id=todo_id, text=text)
    await todo_service.update_todo(todo_dto)
    return RedirectResponse(url="/todos", status_code=status.HTTP_204_NO_CONTENT)
