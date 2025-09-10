import sys
import unittest
from unittest.mock import patch

sys.path.append("..")
from services.user_access import UserAccess

class TestUSerAccess(unittest.TestCase):
    """ Test user login/logout/signup class"""

    def setUp(self):
        """test string out function"""
        self.user_access = UserAccess()


    # --------------USER REGISTRATION--------------
    def test_successful_user_registration(self):
        """test successful user registration"""


    def test_unsuccessful_user_registration(self):
        """test unsuccessful user registration"""


    def test_registration_with_missing_fields(self):
        """test registration with missing username/password"""


    def test_registration_with_invalid_email_format(self):
        """test registration with invalid email"""


    def test_registration_with_weak_password(self):
        """test registration with weak/short password"""

    @patch('services.user_access.DatabaseManager')
    def test_registration_with_existing_user(self, MockDB):
        """test registration with duplicate username/email"""
        mock_db = MockDB.return_value
        mock_db.execute_query.return_value = [] # empty list means no user was found
        result = self.user_access.check_existing_user(username="someUser", email="someEmail@gmail.com")
        self.assertFalse(result)

    def test_registration_db_error(self):
        """test registration fails due to DB error"""


    # --------------LOGIN-----------------
    def test_successful_login(self):
        """test successful user login"""


    def test_failed_login_invalid_credentials(self):
        """test login with wrong username/password"""


    def test_login_with_inactive_user(self):
        """test login with inactive/deleted user"""


    def test_multiple_failed_login_attempts(self):
        """test account lockout after multiple failed login attempts"""


    def test_login_session_created(self):
        """test login session creation"""


    def test_login_db_error(self):
        """test login fails due to DB error"""


    # -------------SESSION-----------------
    def test_successful_session_activation(self):
        """test successful session activation"""


    def test_failed_session_activation_invalid_token(self):
        """test failed session activation with invalid/expired token"""


    # --------------LOGOUT-----------------
    def test_successful_logout(self):
        """test successful user logout"""


    def test_failed_logout_invalid_session(self):
        """test unsuccessful user logout"""


    def test_successful_session_deactivation(self):
        """test successful session deactivation"""


    def test_failed_session_deactivation(self):
        """test unsuccessful session deactivation"""


if __name__ == "__main__":
    unittest.main()
