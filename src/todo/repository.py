""" Todo Repository """

from typing import List

from src.todo.models import Todo

todos = [
    Todo("test"),
    Todo("test1"),
    Todo("test2"),
    Todo("test3"),
]


class TodoRepository:
    """Todo repository class"""

    async def get_todos(self) -> List[Todo]:
        """Retrieve all todos"""
        return todos

    async def create_todo(self, todo: Todo) -> None:
        """Create Todo"""
        todos.append(todo)

    async def update_todo(self, todo_id: str, text: str) -> None:
        """Update Todo"""
        for _, todo_db in enumerate(todos):
            if str(todo_db.id) == todo_id:
                todo_db.text = text
                break
