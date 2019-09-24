import pytest
import removeInstructor_notPass

# For Administrator's remove instructors function
# This will test if the instructor is currently have courses.
def test_remove_instructor():
    assert removeInstructor_notPass.get_instructor_class() == True
