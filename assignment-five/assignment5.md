**Five Test**<br><br>
Test 1: For Students' login function, test if students' user name and password match.<br>
Test 2: For Students' upload files function, test if file types meet requirements.<br>
Test 3: For TA' search students function, test if the student is in the course.<br>
Test 4: For Administrator's add instructors function, test if the type of user to be added is instructors.<br>
Test 5: For Administrator's remove instructors function, test if the instructor is currently have courses.<br>
<br>
**Five Python files that fail these tests**<br>
1. def test_Ismatch(Input_username, Input_password, username_InDatabase, password_InDatabase):
	assert (Input_username == username_InDatabase && Input_password == password_InDatabase)

**Five Python files that pass these tests**<br>

