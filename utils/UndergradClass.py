from .StudentClass import Student

class Undergraduate(Student):
    def __init__(self, name:str, year:int, undergradCourse:str):
        super().__init__(name, year)
        self.__course__ = undergradCourse
        self.__studentType__ = "Undergraduate"
        
    # Setters #
    def setCourse(self, newUndergradCourse):
        self.__course__ = newUndergradCourse
        
    # Getters #
    def getCourse(self):
        return self.__course__
    
    # Serialisation of class #
    def serializeStudent(self):
        # create a string-equivalent of the class, with '-' as its' separators
        serializedClass = f"""
        {self.__studentType__}
        -{self._studyYear_}
        -{self._uniqueId_}
        -{self.__course__}
        -{self._name_}"""
        
        return serializedClass