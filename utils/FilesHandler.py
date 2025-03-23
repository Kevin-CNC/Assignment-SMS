from pathlib import Path
from .StudentClass import Student
from .ReturningThreadClass import ValueReturningThread
import threading as T
import math

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
    
    underGFile = open(undergraduatePath,"r+")
    for line in underGFile:
        # 0: Type (undergraduate), 1: Year of study, 2: Unique Id, 3: Course ID, 4: Full name
        fields = line.split("-") # turns current string into a list with "-" as the separator
        fields[4] = fields[4].strip()
        dataList.append(fields)
    underGFile.close()
    
        
    postGFile = open(postgraduatePath,"r+")
    for line in postGFile:
        # 0: Type (postgrad), 1: Year of study, 2: Unique Id, 3: Already-finished course, 4: Old university, 5: Current Postgrad course, 6: name
        fields = line.split("-") # turns current string into a list with "-" as the separator
        fields[6] = fields[6].strip()
        dataList.append(fields)
    postGFile.close()
        
    return dataList
    

def _findInFrameById_(dataFrame:list,id:str): # all data in text file will be text-based; do not expect to find actual integers
    for item in dataFrame: # remember, 'item' will be a list object (nested lists)
        studentId = item[2]
        if studentId == id:
            return item
    
    return None
    
    
def deleteUserFromFiles(studentInfo:list): 
    if studentInfo[0] == "Undergraduate":
        
        undergraduatePath = filePaths.get("Undergraduates")
        underGFile = open(undergraduatePath,"r+")
        
        underGList = list()
        
        for line in underGFile:
            # 0: Type (undergraduate), 1: Year of study, 2: Unique Id, 3: Course ID, 4: Full name
            fields = line.split("-") # turns current string into a list with "-" as the separator
            fields[4] = fields[4].strip()
            underGList.append(fields)
        underGFile.close()
        
        index = 0
        for studentInfo in underGList:
            if studentInfo[3] == studentInfo[3]: # share same id; must be same student
                underGList.pop(index)
                break
            index += 1
        
        underGFile = open(undergraduatePath,"w+")
        for studentInfo in underGList:
            actualData = studentInfo[0]+"-"+str(studentInfo[1])+"-"+studentInfo[2]+"-"+studentInfo[3]+"-"+studentInfo[4]+"\n"
            underGFile.write(actualData)
        underGFile.close()
        
    elif studentInfo[0] == "Postgraduate":
        postgraduatePath = filePaths.get("Postgraduates")
        postGFile = open(postgraduatePath,"r+")
        
        postGList = list()
        
        for line in postGFile:
            # 0: Type (postgrad), 1: Year of study, 2: Unique Id, 3: prev Course ID, 4: prev uni name, 5: current postgrad course, 6: full name
            fields = line.split("-") # turns current string into a list with "-" as the separator
            fields[6] = fields[6].strip()
            postGList.append(fields)
        postGFile.close()
        
        index = 0
        for studentInfo in postGList:
            if studentInfo[3] == studentInfo[3]: # share same id; must be same student
                postGList.pop(index)
                break
            
            index += 1
        
        postGFile = open(postgraduatePath,"w+")
        for studentInfo in postGList:
            actualData = studentInfo[0]+"-"+str(studentInfo[1])+"-"+studentInfo[2]+"-"+studentInfo[3]+"-"+studentInfo[4]+"-"+studentInfo[5]+"-"+studentInfo[6]+"\n"
            postGFile.write(actualData)
            
        postGFile.close()
        
        
    
def replaceUndergradInFile(undergradInfo:list): # gathers all data from undergrad file, replaces affected student, rewrites it back into the file
    undergraduatePath = filePaths.get("Undergraduates")
    underGFile = open(undergraduatePath,"r+")
    
    underGList = list()
    
    for line in underGFile:
        # 0: Type (undergraduate), 1: Year of study, 2: Unique Id, 3: Course ID, 4: Full name
        fields = line.split("-") # turns current string into a list with "-" as the separator
        fields[4] = fields[4].strip()
        underGList.append(fields)
    underGFile.close()
    
    index = 0
    for studentInfo in underGList:
        if undergradInfo[3] == studentInfo[3]: # share same id; must be same student
            underGList.pop(index)
            underGList.insert(index,undergradInfo)
            break
        
        index += 1
    
    underGFile = open(undergraduatePath,"w+")
    for studentInfo in underGList:
        actualData = studentInfo[0]+"-"+str(studentInfo[1])+"-"+studentInfo[2]+"-"+studentInfo[3]+"-"+studentInfo[4]+"\n"
        underGFile.write(actualData)
        
    underGFile.close()

    
def replacePostgradInFile(postgradInfo:list): # gathers all data from undergrad file, replaces affected student, rewrites it back into the file
    postgraduatePath = filePaths.get("Postgraduates")
    postGFile = open(postgraduatePath,"r+")
    
    postGList = list()
    
    for line in postGFile:
        # 0: Type (postgrad), 1: Year of study, 2: Unique Id, 3: prev Course ID, 4: prev uni name, 5: current postgrad course, 6: full name
        fields = line.split("-") # turns current string into a list with "-" as the separator
        fields[6] = fields[6].strip()
        postGList.append(fields)
    postGFile.close()
    
    index = 0
    for studentInfo in postGList:
        if postgradInfo[3] == studentInfo[3]: # share same id; must be same student
            postGList.pop(index)
            postGList.insert(index,postgradInfo)
            break
        
        index += 1
    
    postGFile = open(postgraduatePath,"w+")
    for studentInfo in postGList:
        actualData = studentInfo[0]+"-"+str(studentInfo[1])+"-"+studentInfo[2]+"-"+studentInfo[3]+"-"+studentInfo[4]+"-"+studentInfo[5]+"-"+studentInfo[6]+"\n"
        postGFile.write(actualData)
        
    postGFile.close()
    
    
    
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
    
    
def findStudentAlgorithm(searchKey:str): # user will be able to choose between 2 modes (Name & UniqueID)
    # main idea behind algorithms:
    # accumulate all in 1 list
    # in both cases, split list into chunks large enough that would produce 5 or less child processes
    all_students = list()
    
    all_students = __getRawFromAll__()

    # Start at 1; conditions check if the amount of child processes produced will not exceed 5.
    foundMax = 1
    while True:
        if len(all_students)%foundMax == 0 and len(all_students)/foundMax <= 5:
            break
        else:
            foundMax += 1
            
    last_anchor_point = 0
    
    resultsCapsules=[None] * 5 # empty result cells for the threads to return the found student

    if foundMax == len(all_students):
        for i in range(4):
            d_frame = list()
            
            frameCeiling = math.floor(len(all_students)/5) # rounds down numbers so elements are split equally in the first 4 frames
            
            for dataIndex in range(last_anchor_point,frameCeiling*i+1):
                d_frame.append( all_students[dataIndex] )
                
            last_anchor_point = frameCeiling*i+1
            
            current_T = ValueReturningThread(target=_findInFrameById_,args=([d_frame,searchKey]))
            current_T.start()
            resultsCapsules[i] = current_T.join() # waits until the thread ends and returns result into its' respective capsule
        
        
        final_DFrame = list()
        # put remaining data in the last frame
        for dataIndex in range(last_anchor_point,len(all_students)):
                final_DFrame.append( all_students[dataIndex] )
                
        
        current_T = ValueReturningThread(target=_findInFrameById_,args=([final_DFrame,searchKey]))
        current_T.start()
        resultsCapsules[4] = current_T.join() # waits until the thread ends and returns result into its' respective capsule
                
    else:
        for i in range(round(len(all_students)/foundMax)):
            d_frame = list()
                    
            for x in range(last_anchor_point,foundMax*(i+1)):
                if x > len(all_students):
                    break
                
                d_frame.append( all_students[x] )
                
            last_anchor_point = (foundMax*(i+1))
            
            current_T = ValueReturningThread(target=_findInFrameById_,args=([d_frame,searchKey]))
            current_T.start()
            resultsCapsules[i] = current_T.join() # waits until the thread ends and returns result into its' respective capsule
    
    # returns results for actual processing
    return(resultsCapsules)
            
