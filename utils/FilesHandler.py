from pathlib import Path
from .StudentClass import Student
from .PostgraduateClass import Postgraduate
from .UndergradClass import Undergraduate
import threading as T

# Referencing the Student_System directory through this script's current position
mainDirectory = Path(__file__).resolve().parent.parent

# Actual text files
filePaths = {
    "Undergraduates":f"{mainDirectory}/student_files/UndergradData.txt",
    "Postgraduates":f"{mainDirectory}/student_files/PostgradData.txt"
}

def __getRawFromAll__():
    dataList = list()
    undergraduatePath = filePaths.get("Undergraduates")
    postgraduatePath = filePaths.get("Postgraduates")
    
    # TODO
        
    
    
    
    
    

def fetchDataFromFile(targetGrade:str): # Doesn't require a check since the user will only have a choice between the 2
    try:
        targetPath = filePaths.get(targetGrade)
        studentFile = open(targetPath,"r")
        # Returns file content
        content = f"{targetGrade} Section:\n" + studentFile.read()
        studentFile.close()
        
        return content
    except Exception as e:
        raise(e) # Automatically raises it to the main script

def writeToFile(targetGrade:str,targetToWrite:Student): # Doesn't require a check since the user will only have a choice between the 2
    targetPath = filePaths.get(targetGrade)
    studentFile = open(targetPath,"a")
    
    studentFile.write(f"\n{targetToWrite.serializeStudent()}")
    studentFile.close()

# Fetches from every student tgrade, through the usage of 'fetchDataFromFile'
def fetchAllData():
    try:
        content = fetchDataFromFile("Undergraduates") + "\n" + fetchDataFromFile("Postgraduates")
        return content
    except Exception as e:
        raise(e)
    
    
def findStudentAlgorithm(searchMode:int): # user will be able to choose between 2 modes (Name & UniqueID)
    # main idea behind algorithms:
    # accumulate all in 1 list
    # in both cases, split list into closest number of chunks possible and create different threads for each chunk
    # TODO
    print("mns")