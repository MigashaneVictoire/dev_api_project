"""User access management file"""
from flask import session

class UserAccess:
    """Handles user registration, login, session management, and logout"""

    # --------- USER REGISTRATION ---------
    def register_user(self, username:str, email:str, password:str):
        """Handle user registration"""


    def validate_user_email(self, email:str) :
        """Check email format"""


    def validate_user_password(self, password:str):
        """Check password strength"""


    def check_existing_user(self, username:str, email:str) -> bool:
        """Check if user already exists"""
        return True  #if username and email are in the database


    # --------- LOGIN ---------
    def login_user(self, username:str, password:str):
        """Handle user login"""


    def validate_credentials(self, username:str, password:str) -> bool:
        """Check username and password correctness"""
        return False


    def check_user_active(self, username:str):
        """Verify if user account is active"""


    def track_failed_login_attempts(self, username:str):
        """Track failed login attempts and enforce lockout"""


    def create_session(self, username:str):
        """Create and return a session token for a logged-in user"""
        session["user"] = username


    # --------- SESSION ---------
    def activate_session(self, token):
        """Activate a session using token"""


    def validate_session_token(self, token):
        """Check if session token is valid and not expired"""


    # --------- LOGOUT ---------
    def logout_user(self, token):
        """Handle user logout"""


    def deactivate_session(self, token):
        """Deactivate a session"""
