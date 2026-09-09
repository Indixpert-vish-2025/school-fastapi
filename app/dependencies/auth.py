from fastapi import Header, HTTPException


def get_current_user(user_id: int = Header(...)):

    if user_id != 5:
        raise HTTPException(
            status_code=401,
            detail="Invalid user"
        )

    return {
        "id": 5,
        "name": "Vishal"
    }