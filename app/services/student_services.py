from app.utils.reuse import read_json, write_json

FILE_PATH = "app/data/students.json"


def get_all_students():
    return read_json(FILE_PATH)


def create_student(student):
    students = read_json(FILE_PATH)

    new_id = max([s["id"] for s in students], default=0) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "email": student.email
    }

    students.append(new_student)
    write_json(FILE_PATH, students)

    return new_student


def delete_student(student_id):
    students = read_json(FILE_PATH)

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            write_json(FILE_PATH, students)
            return student

    return None

def update_student(student_id, student):
    students = read_json(FILE_PATH)

    for existing_student in students:
        if existing_student["id"] == student_id:
            existing_student["name"] = student.name
            existing_student["email"] = student.email

            write_json(FILE_PATH, students)

            return existing_student

    return None