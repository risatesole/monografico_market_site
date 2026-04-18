from ..infrastructure.user_repository import UserRepository
from ..dto import CreateUserDTO

class SignupService:

    @staticmethod
    def execute(user_data: CreateUserDTO):
        # Validation
        if not user_data.username:
            raise ValueError("Username is required")

        if not user_data.email:
            raise ValueError("Email is required")

        if not user_data.password:
            raise ValueError("Password is required")

        # Check duplicates
        existing_user = UserRepository.get_by_email(user_data.email)
        if existing_user:
            raise ValueError("User with this email already exists")

        # Create user
        user = UserRepository.create_user(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password
        )

        return user
