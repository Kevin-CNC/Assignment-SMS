from pathlib import Path

# Referencing the Student_System directory through this script's current position
mainDirectory = Path(__file__).resolve().parent.parent

# Actual text files
filePaths = {
    "Undergraduates":f"{mainDirectory}/student_files/UndergradData.txt",
    "Postgraduates":f"{mainDirectory}/student_files/PostgradData.txt"
}

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

def writeToFile(targetGrade:str): # Doesn't require a check since the user will only have a choice between the 2
    print("TODO!")

# Fetches from every student tgrade, through the usage of 'fetchDataFromFile'
def fetchAllData():
    try:
        content = fetchDataFromFile("Undergraduates") + "\n" + fetchDataFromFile("Postgraduates")
        return content
    except Exception as e:
        raise(e)