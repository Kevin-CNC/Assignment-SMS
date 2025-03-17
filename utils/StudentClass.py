import random as R

def generate_id(): # possible IDs: 2,179,240,250,625
    id = "" # id structure: AB012345678
    for i in range(12):
        if i < 2:
            id += chr(R.randint(65,90)) # generates decimal between 65 - 90 and converts it to character 
        else:
            id += str(R.randint(0,9))
            
    return id

class Student():
    def __init__(self, name, year):
        self._name_ = name
        self._uniqueId_ = generate_id() # Id should be unique for each student; Cannot be changed
        self._studyYear_ = year
        
    # Setters #
    def setName(self, newName):
        self._name_ = newName
        
    def setStudyYear(self, newYear):
        self._studyYear_ = newYear
        
    # Getters #
    def getName(self):
        return self._name_
        
    def setStudyYear(self):
        return self._studyYear_
    
    def getId(self):
        return self._uniqueId_
    