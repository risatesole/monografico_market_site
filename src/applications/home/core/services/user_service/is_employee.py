def is_employee(user):
    if user.role == "internal_user":
        return True
    else:
        return False
