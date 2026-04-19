from django.test import TestCase
from django.contrib.auth import get_user_model
from ..module.domain.entities.user.UserEntity import UserEntity
from ..module.application.signup_Service import SignupService

User = get_user_model()

class TestSignupService(TestCase):

    def setUp(self):
        """Set up a base UserEntity for testing."""
        self.valid_user_entity = UserEntity(
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

    def test_execute_creates_user_successfully(self):
        result = SignupService.execute(self.valid_user_entity)
        self.assertEqual(result.email, "tester@example.com")
        db_user = User.objects.get(email="tester@example.com")
        self.assertEqual(db_user.first_name, "Jane")
        self.assertTrue(db_user.check_password("secure_password_123"))

    def test_execute_raises_error_if_email_exists(self):
        User.objects.create_user(
            username="existing", 
            email="tester@example.com", 
            password="old_password"
        )

        with self.assertRaisesMessage(ValueError, "User with this email already exists"):
            SignupService.execute(self.valid_user_entity)

    def test_validation_errors(self):
        """Tests that missing fields trigger ValueErrors."""
        cases = [
            ("first_name", "", "First Name is required"),
            ("email", "", "Email is required"),
            ("password_hash", "", "Password is required"),
        ]

        for field, value, expected_msg in cases:
            with self.subTest(field=field):
                # Temporarily set the field to empty
                original_value = getattr(self.valid_user_entity, field)
                setattr(self.valid_user_entity, field, value)
                
                with self.assertRaisesMessage(ValueError, expected_msg):
                    SignupService.execute(self.valid_user_entity)
                
                # Reset for next iteration
                setattr(self.valid_user_entity, field, original_value)
