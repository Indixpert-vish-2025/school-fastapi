from app.utils.reuse import read_json, write_json

FILE_PATH = "app/data/teachers.json"


def get_all_teachers():
    return read_json(FILE_PATH)


def create_teacher(teacher):
    teachers = read_json(FILE_PATH)

    new_id = max([t["id"] for t in teachers], default=0) + 1

    new_teacher = {
        "id": new_id,
        "name": teacher.name,
        "email": teacher.email
    }

    teachers.append(new_teacher)
    write_json(FILE_PATH, teachers)

    return new_teacher


def update_teacher(teacher_id, teacher):
    teachers = read_json(FILE_PATH)

    for existing_teacher in teachers:
        if existing_teacher["id"] == teacher_id:
            existing_teacher["name"] = teacher.name
            existing_teacher["email"] = teacher.email

            write_json(FILE_PATH, teachers)

            return existing_teacher

    return None


def delete_teacher(teacher_id):
    teachers = read_json(FILE_PATH)

    for teacher in teachers:
        if teacher["id"] == teacher_id:
            teachers.remove(teacher)

            write_json(FILE_PATH, teachers)

            return teacher

    return None