from fastapi import APIRouter, HTTPException

from app.schemas.teacher_schema import Teacher

from app.services.teacher_services import (
    get_all_teachers,
    create_teacher,
    update_teacher,
    delete_teacher
)


router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)


@router.get("/")
def get_teachers():
    return get_all_teachers()


@router.post("/")
def add_teacher(teacher: Teacher):
    return create_teacher(teacher)


@router.put("/{teacher_id}")
def update_teacher_data(teacher_id: int, teacher: Teacher):

    updated_teacher = update_teacher(teacher_id, teacher)

    if updated_teacher is None:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return {
        "message": "Teacher updated successfully",
        "teacher": updated_teacher
    }


@router.delete("/{teacher_id}")
def remove_teacher(teacher_id: int):

    teacher = delete_teacher(teacher_id)

    if teacher is None:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return {
        "message": "Teacher deleted successfully",
        "teacher": teacher
    }