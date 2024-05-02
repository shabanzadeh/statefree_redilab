from models.hash import Hash
def user_serializer(user) -> dict:
    if "password" in user and user["password"]:
        hashed_password = Hash.bcrypt(user["password"])
    else:
        hashed_password = None 

    return {
        'id': str(user["_id"]),
        'name': user["name"],
        'email': user["email"],
        "password": hashed_password
    }


def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]
    