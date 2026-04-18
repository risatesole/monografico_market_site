from django.test import TestCase
from django.contrib.auth import get_user_model
from ..module.infrastructure.user_repository import UserRepository

User = get_user_model()


class UserRepositoryTest(TestCase):

    def setUp(self):
        self.user = UserRepository.create_user(
            username="henry",
            email="henry@example.com",
            password="test123"
        )

    def test_create_user(self):
        user = UserRepository.create_user(
            username="john",
            email="john@example.com",
            password="test123"
        )

        self.assertIsNotNone(user.id)
        self.assertEqual(user.username, "john")
        self.assertEqual(user.email, "john@example.com")
        self.assertTrue(user.check_password("test123"))

    def test_get_by_id(self):
        user = UserRepository.get_by_id(self.user.id)

        self.assertIsNotNone(user)
        self.assertEqual(user.id, self.user.id)

    def test_get_by_email(self):
        user = UserRepository.get_by_email("henry@example.com")

        self.assertIsNotNone(user)
        self.assertEqual(user.email, "henry@example.com")

    def test_update_user(self):
        updated_user = UserRepository.update_user(
            self.user,
            username="updated_name"
        )

        self.assertEqual(updated_user.username, "updated_name")

    def test_delete_user(self):
        user_id = self.user.id

        UserRepository.delete_user(self.user)

        user = UserRepository.get_by_id(user_id)
        self.assertIsNone(user)