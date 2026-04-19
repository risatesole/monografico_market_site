from django.test import TestCase
from ..module.domain.entities.user.UserEntity import UserEntity

class UserEntityTest(TestCase):

    def setUp(self):
        self.user = UserEntity(1,"test@example.com","hash","jhon","doe","2026/04/18","2026/04/18",True,False)

    def test_get_value(self):
        self.assertEqual(self.user.email, "test@example.com")

    def test_set_value(self):
        self.user.password_hash = "new_hash"
        self.assertEqual(self.user.password_hash, "new_hash")
