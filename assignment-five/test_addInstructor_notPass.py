import pytest
import addInstructor_notPass

# For Administrator's add instructors function
# This will test if the type of user to be added is instructor
def test_add_instructor():
    assert addInstructor_notPass.get_instructor_info() == "professor"
