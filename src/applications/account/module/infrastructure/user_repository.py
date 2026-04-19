from django.contrib.auth import get_user_model
from ..domain.entities.user.UserEntity import UserEntity

User = get_user_model()

class UserRepository:

    @staticmethod
    def create_user(user: UserEntity):
        return User.objects.create_user(
            username = "n/a",
            email= user.email,
            password= user.password_hash,
            first_name = user.first_name,
            last_name = user.last_name,
        )
    
    @staticmethod
    def get_by_id(user: UserEntity):
        return User.objects.filter(id=user.id).first()

    @staticmethod
    def get_by_email(user: UserEntity):
        return User.objects.filter(email=user.email).first()

