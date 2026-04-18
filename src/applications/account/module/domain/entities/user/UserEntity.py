class UserEntity:
    def __init__(self, user_id, email, password_hash, first_name, last_name, created_at, updated_at, is_active, is_email_verified):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash  
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_email_verified = is_email_verified

    def get_value(self, key):
        return getattr(self, key, None)

    def set_value(self, key, value):
        setattr(self, key, value)