# users/repository.py
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRepository:

    @staticmethod
    def create_user(username, email, password):
        return User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

    @staticmethod
    def get_by_id(user_id):
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def get_by_email(email):
        return User.objects.filter(email=email).first()

    @staticmethod
    def update_user(user, **kwargs):
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete_user(user):
        user.delete()

