from utils.FilesHandler import fetchAllData
from utils.NumInputHandler import getNumeralInput
from utils.studentsHandler import updateStudentDetails, deleteStudentDetails, addNewStudent          
from utils.menuPrinter import printMainMenu

## MAIN PROGRAM HERE ##
printMainMenu()
InProgram = True

while InProgram:
    userInput = getNumeralInput("Choose your option: ","Invalid, please retry.")
    
    match userInput:
        case 1:
            addNewStudent()
        case 2:
            updateStudentDetails()
        case 3:
            deleteStudentDetails()
        case 4:
            print(fetchAllData())
            printMainMenu()
        case 5:
            InProgram = False
            print("Exiting program...")
        case _:
            print("Invalid choice.")

