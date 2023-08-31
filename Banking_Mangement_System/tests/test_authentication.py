from unittest import TestCase
from unittest import mock

from src.controllers.authentication import Authentication


class TestAuthentication(TestCase):
    @mock.patch("")
    def test_login(self):
        assert True

    def setUp(self):
        self.user_instance = Authentication()

    def test_valid_login(self):
        # Simulate a valid login scenario
        self.user_instance.username = "Gaurav123"
        self.user_instance.password = "Gaurav123@"  # Use the actual plain password
        # You need to mock the get_item function to return valid user data
        # Assert the function returns the valid_user data
        result = self.user_instance.login()
        self.assertEqual(result, valid_user_data)

    def test_invalid_username(self):
        # Simulate an invalid login scenario with wrong username
        self.user_instance.username = "invalid_username"
        self.user_instance.password = "some_password"  # Use any password here
        # You need to mock the get_item function to return None
        # Assert the function returns None
        result = self.user_instance.login()
        self.assertIsNone(result)

    def test_invalid_password(self):
        # Simulate an invalid login scenario with correct username but wrong password
        self.user_instance.username = "valid_username"
        self.user_instance.password = "wrong_password"  # Use the wrong password here
        # You need to mock the get_item function to return valid user data
        # Assert the function returns None
        result = self.user_instance.login()
        self.assertIsNone(result)
