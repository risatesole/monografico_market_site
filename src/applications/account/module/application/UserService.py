from ..infrastructure.user_repository import UserRepository 
from ..domain.entities.user.UserEntity import UserEntity 

class SignupService:
    @staticmethod
    def execute(user: UserEntity):
        if not user.first_name:
            raise ValueError("First Name is required")

        if not user.email:
            raise ValueError("Email is required")

        if not user.password_hash:
            raise ValueError("Password is required")

        existing_user = UserRepository.get_by_email(user)

        if existing_user:
            raise ValueError("User with this email already exists")

        UserRepository.create_user(user)

        return user
