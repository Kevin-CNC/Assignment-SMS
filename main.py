from utils.PostgraduateClass import Postgraduate as PostGrad
from utils.UndergradClass import Undergraduate as UnderGrad
from utils.SubjectsDatabase import *
from utils.FilesHandler import *


def printMainMenu():
    print("""* In Main Menu *\n
          * Pick one of the following: *
          * 1 - Add a new student
          * 2 - Update student's details
          * 3 - Delete a student
          * 4 - See all students
          * 5 - Exit
          """)

def getNumeralInput(msg,outputmsg):
    userInput = str(input(msg))
    try:
        userInput = int(userInput)    
    except ValueError:
        print(outputmsg)
        return None
    except Exception as e:
        print(f"Something went wrong:\n{e}")
        return None
    
    return(userInput)


def addNewStudent():   
    print("""In student add mode:\n
          What student type you'd like to enter? (Enter 3 to go back to the menu)\n
          * 1 - Undergraduate
          * 2 - Postgraduate
          * 3 - Go back
          """)
    try: 
        while True:
            # 'sam'= student add mode
            sam_Userinput = getNumeralInput("","Invalid choice, try again.")
            
            if sam_Userinput == None:
                continue # Function returns 'None' only if input invalid, hence skip this iteration
            
            elif sam_Userinput < 1 or sam_Userinput > 3:
                continue # same logic, but invalid numbers
            
            elif sam_Userinput == 3: # break point
                print("Returning to main. . .")
                break
            
            elif sam_Userinput == 1: # Adding undergraduate student
                while True:
                    print("Adding undergraduate student details: ")
                    
                    while True: # Student name choice
                        global studentName
                        studentName = str(input("Enter your student's full name (Name Second_Name Surname): "))
                        
                        if studentName.find("-") == -1:
                            break
                        else:
                            print("Invalid name, contains an illegal character.")
                        
                    
                    while True: # Year validation loop
                        global studentYear
                        
                        yearInput = getNumeralInput("Enter student year (1, 2 or 3): ","")
                        if yearInput == None:
                            print("Invalid year; retry.")
                        elif yearInput < 1 or yearInput > 3:
                            print("Invalid year; retry.")
                        else:
                            studentYear = yearInput
                            break
                        
                    print("Add undergraduate's course ID (Enter 1 if you wish to have a list of all undergraduate courses)")
                    showUndergradCourseOption = getNumeralInput("","")
                    if showUndergradCourseOption == 1:
                        printAllUndergradCourses()
                        
                    while True: # Course loop
                        global courseId
                        
                        courseIdInput = str(input("Enter course ID: "))
                        if Courses["Undergraduate"].get(courseIdInput) == None:
                            print("Invalid ID, press 1 if you would like to have a list of all undergraduate courses, anything else to directly retry")
                            showUndergradCourseOption = getNumeralInput("","")
                            if showUndergradCourseOption == 1:
                                printAllUndergradCourses()   
                        else:
                            courseId = courseIdInput
                            break
                            
                            
                    print(f"Here are the finalised details:\nYour student is an: Undergraduate;\nYour student's full name is: {studentName};\nYour student's current year: {studentYear};\nYour student's course is: {Courses["Undergraduate"][courseId]};\n\nEnter 1 to confirm this student's details, press 2 to retry the process, anything else to directly go back to main menu.")
                    
                    userChoice = getNumeralInput("","Invalid choice, try again.")
                    if userChoice == 1: # Confirmation; can add to database
                        confirmedStudent = UnderGrad(studentName,studentYear,courseId)
                        writeToFile("Undergraduates",confirmedStudent)
                        
                        print("Student added, going back to main menu...")
                        printMainMenu()
                        break
                    elif userChoice == 2: # Retry; Skip this iteration
                        continue
                    else:
                        break
                    
                    
            elif sam_Userinput == 2: # Adding postgraduate student
                while True:
                    print("Adding postgraduate student details: ")
                    
                    while True: # Student name choice
                        global postStudentName
                        postStudentName = str(input("Enter your student's full name (Name Second_Name Surname): "))
                        
                        if postStudentName.find("-") == -1:
                            break
                        else:
                            print("Invalid name, contains an illegal character.")
                        
                    print("What course have they completed?\nIf their course is also offered in this institution, enter its' ID from the already-existing courses database.\nElse, please enter 'Other' .\n(Enter 1 if you wish to have a list of all undergraduate courses, else anything else to not display them.)")
                    showUndergradCourseOption = getNumeralInput("","")
                    if showUndergradCourseOption == 1:
                        printAllUndergradCourses()
                        
                    while True: # Previous course loop
                        global completedCourse
                        
                        courseIdInput = str(input("Enter course ID: "))
                        if courseIdInput == "other" or courseIdInput == "Other" or courseIdInput == "OTHER":
                            completedCourse = "Other"
                            break
                        elif Courses["Undergraduate"].get(courseIdInput) == None:
                            print("Invalid choice, press 1 if you would like to have a list of all undergraduate courses, anything else to directly retry")
                            showUndergradCourseOption = getNumeralInput("","")
                            if showUndergradCourseOption == 1:
                                printAllUndergradCourses()   
                        else:
                            completedCourse = Courses["Undergraduate"].get(courseIdInput)
                            break
                        
                        
                    # Previous university name
                    while True:
                        global prevUniName
                        print("Enter their previous university's name:")
                        prevUniName = str(input(""))
                        
                        if prevUniName.find('-') == -1: # returns -1 upon failure of finding the character
                            break
                        else:
                            print("Illegal character found (-); Avoid using this character.")
                        
                    
                    print("What postgraduate course are they enrolled in?\nEnter 1 if you'd like to be given a list of all postgraduate courses available (Anything else to skip).")
                    showPostgradCourses = getNumeralInput("","")
                    if showPostgradCourses == 1:
                        printAllPostgradCourses()
                
                    while True: # Current Course loop
                        global postgradCourseId
                        
                        courseIdInput = str(input("Enter course ID: "))
                        if Courses["Postgraduate"].get(courseIdInput) == None:
                            print("Invalid ID, press 1 if you would like to have a list of all postgraduate courses, anything else to directly retry")
                            showUndergradCourseOption = getNumeralInput("","")
                            if showUndergradCourseOption == 1:
                                printAllPostgradCourses()   
                        else:
                            postgradCourseId = courseIdInput
                            print("a")
                            break
                        
                    
                    print(f"Here are the finalised details:\nYour student is an: Postgraduate;\nYour student's name is: {postStudentName};\nYour student's course is: {Courses["Postgraduate"][postgradCourseId]};\nYour student completed the undergraduate course: {completedCourse};\nYour student completed their undergraduate course at the following institution: {prevUniName};\n\nEnter 1 to confirm this student's details, press 2 to retry the process, anything else to directly go back to main menu.")
                
                    userChoice = getNumeralInput("","")
                    if userChoice == 1: # Confirmation; can add to database
                        confirmedStudent = PostGrad(postStudentName,5,completedCourse,prevUniName,postgradCourseId)
                        writeToFile("Postgraduates",confirmedStudent)
                        
                        print("Student added, going back to main menu...")
                        printMainMenu()
                        break
                    elif userChoice == 2: # Retry; Skip this iteration
                        print("Retrying:")
                        continue
                    else:
                        print("Exiting:")
                        printMainMenu()
                        break
                    
                    
    except Exception as e:
        print(e)


def updateStudentDetails():
    print("How do you want to find the student?\n1- By ID\n2- By Full name")
    searchMode = getNumeralInput("","Invalid choice, returning to menu.")
    
    if searchMode == 1 or searchMode == 2:
        dataTarget = str() # used for message prompt
        if searchMode == 1:
            dataTarget = "ID"
        else:
            dataTarget = "Full name"
        print(f"Mode chosen: {dataTarget}")
        
        while True:
            key = str(input(f"Enter the {dataTarget} of the student you'd like to update: "))
            searchResultPool = findStudentAlgorithm(searchMode,key) 
            
            # Process of analysing the results given
            foundTargets = list()
            for result in searchResultPool:
                if not(result == None):
                    foundTargets.append(result)
                    
            
            if len(foundTargets) == 0:
                print("No students found; enter 1 to retry, anything else to exit.")
                choice = getNumeralInput("","Invalid input; exiting mode.")
                if not( choice == 1 ):
                    break
                
            elif len(foundTargets) == 1: # 1 student found
                print(f"Student found: {foundTargets[0]}")
                print("Press 1 to confirm, press 2 to retry, anything else to exit the mode.")
                
                choice = getNumeralInput("","Invalid input; exiting mode.")
                if not( choice == 1 or choice == 2 ):
                    break
                elif choice == 2: # Retries the whole process
                    continue
                elif choice == 1:
                    studentToModify = foundTargets[0]
                    modified = False
                    if studentToModify[0] == "Undergraduate":
                        print("""Please choose what to modify:\n
                              1- Student's Name\n
                              2- Student's current course\n
                              3- Student's study year\n
                              4- Exit""")
                        while True: # Entered student modification mode
                            optionChoice = getNumeralInput("","Invalid option, try again...")
                            
                            if optionChoice == 1: # Name choice
                                while True: # choice loop
                                    newName = str(input("Enter your student's new name: "))
                                    
                                    if newName.find("-") == -1: # not an illegal name
                                        print(f"Your student's new chosen name is: {newName}; Do you wish to apply it to your student? (old name:{studentToModify[4]})")
                                        confirmation = getNumeralInput("1 for Yes; anything else for no\n","Invalid command; abort change of name.")
                                        
                                        if not( confirmation == 1):
                                            continue # Skip current iteration; go back to name choice
                                        else:
                                            studentToModify[4] = newName # Apply change and break from current choice-loop
                                            modified = True
                                            break
                                        
                            elif optionChoice == 2: # Course choice                                        
                                while True:
                                    printAllUndergradCourses()
                                    
                                    newCourseID = str(input("Enter course ID: "))
                                    if Courses["Undergraduate"].get(newCourseID) == None:
                                        print("Invalid course, try again.")
                                        continue
                                    else:
                                        print(f"Your student's new course is: {newCourseID} - {Courses["Undergraduate"].get(newCourseID)}; Do you wish to apply it to your student? (old course:{studentToModify[3] - {Courses["Undergraduate"].get(studentToModify[3])}})")
                                        confirmation = getNumeralInput("1 for Yes; anything else for no\n","Invalid command; abort change of course.")
                                        if not( confirmation == 1):
                                            continue # Skip current iteration; go back to name choice
                                        else:
                                            studentToModify[3] = newCourseID # Apply change and break from current choice-loop
                                            modified = True
                                            break
                                        
                                        
                            elif optionChoice == 3: # Year choice
                                while True: # choice loop
                                    newYear = getNumeralInput("Enter your student's new year (1 - 3): ","Not a valid number...")
                                    
                                    if 0 < newYear < 4: # not an illegal name
                                        print(f"Your student's new year is: {newYear}; Do you wish to apply it to your student? (old study year:{studentToModify[1]})")
                                        confirmation = getNumeralInput("1 for Yes; anything else for no\n","Invalid command; abort change of year.")
                                        
                                        if not( confirmation == 1):
                                            continue # Skip current iteration; go back to name choice
                                        else:
                                            studentToModify[1] = newYear # Apply change and break from current choice-loop
                                            modified = True
                                            break
                            
                            elif optionChoice == 4:
                                break
                                        
                            elif optionChoice == None:
                                continue # invalid, stay in current modification loop
                            
                            print(f"New student details:\n{studentToModify}")
                            print("""Please choose what to modify:\n
                              1- Student's Name\n
                              2- Student's current course\n
                              3- Student's study year\n
                              4- Exit""")
                            
                            
                        if modified: # modifications actually applied
                            replaceUndergradInFile(studentToModify)
                            break
                            
                            
                
            
                
        print("Exiting update student mode...")
        printMainMenu()
                
            
            
            
    

## MAIN PROGRAM HERE ##
printMainMenu()
InProgram = True

while InProgram:
    userInput = getNumeralInput("Choose your option: ","Invalid, please retry.")
    
    match userInput:
        case 1:
            addNewStudent()
            break
        case 2:
            updateStudentDetails()
        case 4:
            print(fetchAllData())
        case 5:
            InProgram = False
            print("Exiting program...")
            break
        case _: # Default case, use this if the user input is not valid
            break
