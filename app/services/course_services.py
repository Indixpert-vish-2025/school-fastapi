from app.utils.reuse import read_json, write_json

FILE_PATH = "app/data/courses.json"


def get_all_courses():
    return read_json(FILE_PATH)


def create_course(course):
    courses = read_json(FILE_PATH)

    new_id = max([c["id"] for c in courses], default=0) + 1

    new_course = {
        "id": new_id,
        "name": course.name,
        "teacher_id": course.teacher_id
    }

    courses.append(new_course)
    write_json(FILE_PATH, courses)

    return new_course


def update_course(course_id, course):
    courses = read_json(FILE_PATH)

    for existing_course in courses:
        if existing_course["id"] == course_id:
            existing_course["name"] = course.name
            existing_course["teacher_id"] = course.teacher_id

            write_json(FILE_PATH, courses)

            return existing_course

    return None


def delete_course(course_id):
    courses = read_json(FILE_PATH)

    for course in courses:
        if course["id"] == course_id:
            courses.remove(course)

            write_json(FILE_PATH, courses)

            return course

    return None