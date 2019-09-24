import pytest
import addInstructor_pass

# For Administrator's add instructors function
# This will test if the type of user to be added is instructor
def test_add_instructor():
    assert addInstructor_pass.get_instructor_info() == "professor"
