from django.test import TestCase
from ..module.domain.entities.user.UserEntity import UserEntity


class UserEntityTest(TestCase):

    def setUp(self):
        self.user = UserEntity(
            user_id=1,
            email="test@example.com",
            password_hash="old_hash",
            first_name="Henry",
            last_name="Ramirez",
            created_at="2026-01-01",
            updated_at="2026-01-01",
            is_active=True,
            is_email_verified=False
        )

    def test_get_value(self):
        self.assertEqual(self.user.get_value("email"), "test@example.com")

    def test_set_value(self):
        self.user.set_value("password_hash", "new_hash")
        self.assertEqual(self.user.get_value("password_hash"), "new_hash")

    def test_invalid_key(self):
        self.assertIsNone(self.user.get_value("does_not_exist"))
