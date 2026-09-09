from fastapi import APIRouter, HTTPException

from app.schemas.course_schema import Course

from app.services.course_services import (
    get_all_courses,
    create_course,
    update_course,
    delete_course
)


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get("/")
def get_courses():
    return get_all_courses()


@router.post("/")
def add_course(course: Course):
    return create_course(course)


@router.put("/{course_id}")
def update_course_data(course_id: int, course: Course):

    updated_course = update_course(course_id, course)

    if updated_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {
        "message": "Course updated successfully",
        "course": updated_course
    }


@router.delete("/{course_id}")
def remove_course(course_id: int):

    course = delete_course(course_id)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {
        "message": "Course deleted successfully",
        "course": course
    }