""" DTOs """

# from uuid import uuid4

from typing import Optional

from pydantic import BaseModel


class TodoDTO(BaseModel):
    """
    TodoDTO
    """

    id: Optional[str] = None
    text: Optional[str] = None
    done: Optional[bool] = None

    # def __init__(self, text: str) -> None:
    #     # self.id = uuid4()
    #     self.id: Optional[str] = None
    #     self.text: Optional[str] = text
    #     self.done = False
