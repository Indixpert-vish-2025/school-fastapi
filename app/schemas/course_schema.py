from pydantic import BaseModel


class Course(BaseModel):
    name: str
    teacher_id: int | None = None