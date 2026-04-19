class UserEntity:
    def __init__(self, user_id: int, email:str, password_hash:str, first_name:str, last_name:str, created_at:str , updated_at:str, is_active:bool, is_email_verified:bool):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash  
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_email_verified = is_email_verified
