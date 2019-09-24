import pytest
import login_pass

# For Students' login function
# This will test if users' name and password match the data in database
def test_login_pass():
    usernameInDB = "user"
    passwordInDB = "password"  
    assert login_pass.get_login_password() == passwordInDB and login_pass.get_login_username() == usernameInDB

