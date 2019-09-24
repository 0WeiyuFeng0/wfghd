import pytest
import search_notPass

# For TA' search students function
# This will test if TA is going to find the student
def test_search_student():
    assert search_notPass.get_student_search_result() > 0
