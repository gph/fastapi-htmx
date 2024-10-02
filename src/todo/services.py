""" Todo Service """

from src.todo.repository import TodoRepository


class TodoService:
    """Todo Service"""

    def __init__(self, todo_repository: TodoRepository) -> None:
        self.todo_repository = todo_repository

    async def get_todos(self):
        """Retrieve all todos"""
        return self.get_todos()
