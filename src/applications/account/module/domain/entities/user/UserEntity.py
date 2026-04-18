class UserEntity:
    def __init__(self, user_id, email, passwordhash, first_name, last_name, created_at, updated_at,is_active,is_email_verified):
        self.user_id = user_id
        self.email = email
        self.passwordhash = passwordhash  
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_email_verified = is_email_verified
