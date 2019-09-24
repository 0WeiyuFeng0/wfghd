import pytest
import fileType_notPass

#For Students' upload files function
# This will test if the type of uploaded file is valid
def test_fileType_pass():
    IsCorrectFileType = False
    requiredFileType = ["txt","pdf","md"]  
    for fileType in requiredFileType:  
        if fileType_notPass.get_fileType() == fileType:
            IsCorrectFileType = True
    assert IsCorrectFileType == True
