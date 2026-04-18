import uuid

class UserEntity:
    def __init__(self, user_id, username, email, passwordhash, first_name, last_name, created_at, updated_at):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.passwordhash = passwordhash  
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = True
        self.created_at = created_at
        self.updated_at = updated_at

        self.is_email_verified = False
        self.email_verification_token = str(uuid.uuid4())

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def isactive(self):
        return self.is_active

    def update_email(self, new_email):
        self.email = new_email
        self.is_email_verified = False
        self.email_verification_token = str(uuid.uuid4())

    def verify_email(self, token):
        if self.email_verification_token != token:
            raise ValueError("Invalid verification token")

        self.is_email_verified = True
        self.email_verification_token = None

    def update_password(self, old_password, new_password):
        if self.passwordhash != old_password:
            raise ValueError("Old password is incorrect")
        self.passwordhash = new_password

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name

    def __repr__(self):
        return (
            f"User(id={self.user_id}, username='{self.username}', "
            f"name='{self.first_name} {self.last_name}', "
            f"email='{self.email}', active={self.is_active}, "
            f"verified={self.is_email_verified})"
        )
