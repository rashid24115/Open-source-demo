def validate_username(username):
    if len(username) < 3:
        print("Invalid username: Too short!")
        return False
    print("Username is valid!")
    return True
