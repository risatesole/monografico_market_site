"""
Warning: tests are not done
Warning tests are incomplete
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from ..module.infrastructure.user_repository import UserRepository as UserRepository
from ..module.domain.entities.user.UserEntity import UserEntity

User = get_user_model()


class UserRepositoryTest(TestCase):

    def setUp(self):
        self.user: UserEntity = UserEntity(
            id=1,
            email="tester@example.com",
            password_hash="secure_password_123",
            first_name="Jane",
            last_name="Doe",
            created_at="2026-04-18",
            updated_at="2026-04-18",
            is_active=True,
            is_email_verified=False
        )
