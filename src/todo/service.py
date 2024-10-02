""" Todo Service """

from typing import List

from fastapi import Depends

from src.todo.models import Todo
from src.todo.repository import TodoRepository
from src.todo.schemas import TodoDTO


class TodoService:
    """Todo Service"""

    def __init__(
        self, todo_repository: TodoRepository = Depends(TodoRepository)
    ) -> None:
        self.todo_repository = todo_repository

    async def get_todos(self) -> List[Todo]:
        """Retrieve all todos"""

        return await self.todo_repository.get_todos()

    async def create_todo(self, todo_dto: TodoDTO) -> None:
        """Create todo"""

        todo = Todo(text=todo_dto.text)
        await self.todo_repository.create_todo(todo)

    async def update_todo(self, todo_dto: TodoDTO) -> None:
        """Update todo"""

        todos = await self.todo_repository.get_todos()
        for _, todo in enumerate(todos):
            if str(todo.id) == todo_dto.id:
                todo.text = todo_dto.text
                break
