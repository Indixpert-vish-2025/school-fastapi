from fastapi import APIRouter, HTTPException, Depends
from app.dependencies.auth import get_current_user
from app.schemas.student_schema import Student
from app.services.student_services import (
    get_all_students,
    create_student,
    delete_student,
    update_student
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/")
def get_students(current_user=Depends(get_current_user)):
    return {
        "current_user": current_user,
        "students": get_all_students()
    }


@router.post("/")
def add_student(student: Student):
    return create_student(student)

@router.put("/{student_id}")
def update_student_data(student_id: int, student: Student):
    updated_student = update_student(student_id, student)

    if updated_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student updated successfully",
        "student": updated_student
    }


@router.delete("/{student_id}")
def remove_student(student_id: int):
    student = delete_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully",
        "student": student
    }