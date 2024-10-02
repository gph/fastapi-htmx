""" Todo Repository """

from src.todo.schemas import Todo

todos = [
    Todo("test"),
    Todo("test1"),
    Todo("test2"),
    Todo("test3"),
]


class TodoRepository:
    """Todo repository class"""

    async def get_todos(self) -> list[Todo]:
        """Retrieve all todos"""
        return todos

    async def create_todo(self, todo: Todo) -> None:
        """Create Todo"""
        todos.append(todo)
