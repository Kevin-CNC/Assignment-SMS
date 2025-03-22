from .StudentClass import Student

class Postgraduate(Student):
    def __init__(self, name:str, year:int,alreadyFinishedCourse:str,previousUniversity:str,postGradCourse:str):
        super().__init__(name, year)
        self.__finishedCourse__ = alreadyFinishedCourse
        self.__previousUniversity__ = previousUniversity
        self.__course__ = postGradCourse
        self.__studentType__ = "Postgraduate"
        
    # Setters #
    def setFinishedCourse(self, newFinished):
        self.__finishedCourse__ = newFinished
    
    def setNewCourse(self, newCourse):
        self.__course__ = newCourse
    
    def setPreviousUni(self, newPrevUni):
        self.__finishedCourse__ = newPrevUni
        
    # Getters #
    def getFinishedCourse(self):
        return self.__finishedCourse__
    
    def getPreviousUni(self):
        return self.__finishedCourse__
    
    def getCourse(self):
        return self.__course__
    
    def serializeStudent(self):
        # create a string-equivalent of the class, with '-' as its' separators
        serializedClass = f"""{self.__studentType__}-{self._studyYear_}-{self._uniqueId_}-{self.__finishedCourse__}-{self.__previousUniversity__}-{self.__course__}-{self._name_}"""
        
        return serializedClass