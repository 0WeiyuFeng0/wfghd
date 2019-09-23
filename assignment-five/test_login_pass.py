import pytest
import main

# This will pass the test
def test_login_pass():
    usernameInDB = "user"
    passwordInDB = "password"  
    assert main.get_login_password() == passwordInDB and main.get_login_username() == usernameInDB

