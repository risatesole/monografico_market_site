from django.test import TestCase
from django.contrib.auth import get_user_model
from ..module.application.UserService import SignupService
from ..module.dto.create_user_dto import CreateUserDTO

User = get_user_model()

class SignupServiceTest(TestCase):

    def test_successful_signup(self):
        dto = CreateUserDTO(
            username="henry",
            email="henry@example.com",
            password="secure123"
        )

        user = SignupService.execute(dto)

        self.assertIsNotNone(user.id)
        self.assertEqual(user.username, "henry")
        self.assertEqual(user.email, "henry@example.com")
        self.assertTrue(user.check_password("secure123"))

    def test_signup_missing_username(self):
        dto = CreateUserDTO(
            username="",
            email="henry@example.com",
            password="secure123"
        )

        with self.assertRaises(ValueError) as context:
            SignupService.execute(dto)

        self.assertEqual(str(context.exception), "Username is required")

    def test_signup_missing_email(self):
        dto = CreateUserDTO(
            username="henry",
            email="",
            password="secure123"
        )

        with self.assertRaises(ValueError) as context:
            SignupService.execute(dto)

        self.assertEqual(str(context.exception), "Email is required")

    def test_signup_missing_password(self):
        dto = CreateUserDTO(
            username="henry",
            email="henry@example.com",
            password=""
        )

        with self.assertRaises(ValueError) as context:
            SignupService.execute(dto)

        self.assertEqual(str(context.exception), "Password is required")

    def test_signup_duplicate_email(self):
        # Create initial user
        User.objects.create_user(
            username="existing",
            email="henry@example.com",
            password="test123"
        )

        dto = CreateUserDTO(
            username="henry",
            email="henry@example.com",
            password="secure123"
        )

        with self.assertRaises(ValueError) as context:
            SignupService.execute(dto)

        self.assertEqual(
            str(context.exception),
            "User with this email already exists"
        )