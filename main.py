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
          * 4 - Search (See More)
          * 5 - See all students
          * 6 - Exit
          """)

def getNumeralInput(msg):
    userInput = str(input(msg))
    try:
        userInput = int(userInput)    
    except ValueError:
        print("Invalid choice from you; Please try again.")
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
            sam_Userinput = getNumeralInput("")
            
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
                    studentName = str(input("Enter your student's full name (Name Second_Name Surname): "))
                    
                    while True: # Year validation loop
                        global studentYear
                        
                        yearInput = getNumeralInput("Enter student year (1, 2 or 3): ")
                        if yearInput == None:
                            print("Invalid year; retry.")
                        elif yearInput < 1 or yearInput > 3:
                            print("Invalid year; retry.")
                        else:
                            studentYear = yearInput
                            break
                        
                    print("Add undergraduate's course ID (Enter 1 if you wish to have a list of all undergraduate courses)")
                    showUndergradCourseOption = getNumeralInput("")
                    if showUndergradCourseOption == 1:
                        printAllUndergradCourses()
                        
                    while True: # Course loop
                        global courseId
                        
                        courseIdInput = str(input("Enter user ID ('-' character is required): "))
                        if Courses["Undergraduate"].get(courseIdInput) == None:
                            print("Invalid ID, press 1 if you would like to have a list of all undergraduate courses, anything else to directly retry")
                            showUndergradCourseOption = getNumeralInput("")
                            if showUndergradCourseOption == 1:
                                printAllUndergradCourses()   
                        else:
                            courseId = courseIdInput
                            break
                            
                            
                    print(f"""Here are the finalised details:\n
                        Your student is an: Undergraduate;\n
                        Your student's full name is: {studentName};\n
                        Your student's current year: {studentYear};\n
                        Your student's course is: {Courses["Undergraduate"][courseId]};\n
                        Enter 1 to confirm this student's details, press 2 to retry the process, anything else to directly go back to main menu.
                        """)
                    
                    userChoice = getNumeralInput("")
                    if userChoice == 1: # Confirmation; can add to database
                        confirmedStudent = UnderGrad(studentName,studentYear,courseId)
                        # add logic to add to file system
                        
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
                    studentName = str(input("Enter your student's full name (Name Second_Name Surname): "))
                        
                    print("""What course have they completed?\n  
                        If their course is also offered in this institution, enter its' ID from the already-existing courses database (Enter 1 if you wish to have a list of all undergraduate courses).\n
                        Else, please enter 'Other' .""")
                    showUndergradCourseOption = getNumeralInput("")
                    if showUndergradCourseOption == 1:
                        printAllUndergradCourses()
                        
                    while True: # Previous course loop
                        global completedCourse
                        
                        courseIdInput = str(input("Enter user ID ('-' character is required): "))
                        if courseIdInput.lower() == "other":
                            completedCourse = "Other"
                        elif Courses["Undergraduate"].get(courseIdInput) == None:
                            print("Invalid choice, press 1 if you would like to have a list of all undergraduate courses, anything else to directly retry")
                            showUndergradCourseOption = getNumeralInput("")
                            if showUndergradCourseOption == 1:
                                printAllUndergradCourses()   
                        else:
                            completedCourse = Courses["Undergraduate"].get(courseIdInput)
                            break
                        
                        
                    # Previous university name
                    print("Enter their previous university's name:\n")
                    prevUniName = str(input(""))
                        
                    
                    print("""What postgraduate course are they enrolled in?\n  
                        Enter 1 if you'd like to be given a list of all postgraduate courses available.""")
                    showPostgradCourses = getNumeralInput("")
                    if showPostgradCourses == 1:
                        printAllPostgradCourses()
                
                    while True: # Current Course loop
                        global postgradCourseId
                        
                        courseIdInput = str(input("Enter user ID ('-' character is required): "))
                        if Courses["Postgraduate"].get(courseIdInput) == None:
                            print("Invalid ID, press 1 if you would like to have a list of all postgraduate courses, anything else to directly retry")
                            showUndergradCourseOption = getNumeralInput("")
                            if showUndergradCourseOption == 1:
                                printAllPostgradCourses()   
                        else:
                            postgradCourseId = courseIdInput
                            break
                            
                            
                    print(f"""Here are the finalised details:\n
                        Your student is an: Postgraduate;\n
                        Your student's full name is: {studentName};\n
                        Your student's current year: {studentYear};\n
                        Your student's course is: {Courses["Postgraduate"][postgradCourseId]};\n
                        Your student completed the undergraduate course: {completedCourse};\n
                        Your student completed their undergraduate course at the following institution: {prevUniName};\n
                        
                        Enter 1 to confirm this student's details, press 2 to retry the process, anything else to directly go back to main menu.
                        """)
                    
                    userChoice = getNumeralInput("")
                    if userChoice == 1: # Confirmation; can add to database
                        confirmedStudent = PostGrad(studentName,5,completedCourse,prevUniName,courseId)
                        # add logic to add to file system
                        
                        print("Student added, going back to main menu...")
                        printMainMenu()
                        break
                    elif userChoice == 2: # Retry; Skip this iteration
                        continue
                    else:
                        break
    except Exception as e:
        print()


## MAIN PROGRAM HERE ##
printMainMenu()
InProgram = True

while InProgram:
    userInput = getNumeralInput("Choose your option: ")
    
    match userInput:
        case 1:
            addNewStudent()
            break
        case 5:
            print(fetchAllData())
        case 6:
            InProgram = False
            print("Exiting program...")
            break
        case _: # Default case, use this if the user input is not valid
            break
