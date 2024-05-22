def user_schema(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
        "email": user["email"],
        "is_admin": user["is_admin"]}

def users_schema(users) -> list:
    return [user_schema(user) for user in users]