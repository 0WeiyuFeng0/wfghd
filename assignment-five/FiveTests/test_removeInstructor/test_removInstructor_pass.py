import pytest
import removeInstructor_pass

# For Administrator's remove instructors function
# This will test if the instructor is currently have courses.
def test_remove_instructor():
    assert removeInstructor_pass.get_instructor_class() == True
