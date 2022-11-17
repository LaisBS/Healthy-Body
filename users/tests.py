from rest_framework.test import APITestCase
from users.models import User


class UserTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.user_data = {
            "username": "UserTest",
            "first_name": "User",
            "last_name": "Test",
            "phone": "123456789",
            "birthdate": "1998-04-12",
            "is_active": True,
            "password": "12345",
            "email": "test@email.com",
        }

        cls.user = User.objects.create_user(**cls.user_data)

    def test_username_max_length(self):

        max_length = self.user._meta.get_field("username").max_length

        self.assertEqual(max_length, 25)

    def test_email_max_length(self):

        max_length = self.user._meta.get_field("email").max_length

        self.assertEqual(max_length, 127)

    def test_username_unique(self):

        unique = self.user._meta.get_field("username").unique

        self.assertTrue(unique)

    def test_email_unique(self):

        unique = self.user._meta.get_field("email").unique

        self.assertTrue(unique)

    def test_password_max_length(self):

        max_length = self.user._meta.get_field("password").max_length

        self.assertEqual(max_length, 100)

    def test_phone_max_length(self):

        max_length = self.user._meta.get_field("phone").max_length

        self.assertEqual(max_length, 20)

    def test_first_name_max_length(self):

        max_length = self.user._meta.get_field("first_name").max_length

        self.assertEqual(max_length, 50)

    def test_last_name_max_length(self):

        max_length = self.user._meta.get_field("last_name").max_length

        self.assertEqual(max_length, 50)

    def test_is_active_default(self):

        is_active = self.user._meta.get_field("is_active").default

        self.assertTrue(is_active)
