import sys
from flask import url_for, redirect, render_template, request, flash, Blueprint
sys.path.append("..")
from app.services.user_access import UserAccess


# Create a Blueprint for login routes
login_bluePrint = Blueprint('login', __name__)
user_access = UserAccess()

@login_bluePrint.route("/", methods=['POST'])
@login_bluePrint.route("/login/", methods=['POST'])
def login_page():
    """
    Handles user login page rendering.

    :Returns
        flask.Response: Rendered login page or a redirect to the home page upon successful login.
    """
    username = request.form.get("username")
    password = request.form.get("password")

    # grant access
    is_valid_cred = user_access.validate_credentials(username=username, password=password)

    if is_valid_cred:
        # create a session
        user_access.create_session(username=username)
        flash("Login successful!", "success")
        # ----> add a logger here <-------
        return redirect(url_for('home.home_page'))
    return render_template("login.html")