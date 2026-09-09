from app.utils.reuse import read_json, write_json

FILE_PATH = "app/data/users.json"


def create_user(user):
    users = read_json(FILE_PATH)

    # Check email already exists
    for existing_user in users:
        if existing_user["email"].lower() == user.email.lower():
            return None

    new_id = max([u["id"] for u in users], default=0) + 1

    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "role": user.role
    }

    users.append(new_user)

    write_json(FILE_PATH, users)

    return new_user

def login_user(email, password):
    users = read_json(FILE_PATH)

    for user in users:
        if (
            user["email"].lower() == email.lower()
            and user["password"] == password
        ):
            return user

    return None