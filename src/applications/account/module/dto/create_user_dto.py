class CreateUserDTO:
    def __init__(self, first_name : str, last_name : str , email : str, password : str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.email: str = email
        self.password: str = password
