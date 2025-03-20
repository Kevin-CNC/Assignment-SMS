# Rudimentary python database for undergraduate courses and postgraduate courses #

Courses = {
    # Undergraduate Courses
    "Undergraduate":{
        "UG001": "Computer Science",
        "UG002": "Mechanical Engineering",
        "UG003": "Electrical Engineering",
        "UG004": "Civil Engineering",
        "UG005": "Business Administration",
        "UG006": "Psychology",
        "UG007": "Economics",
        "UG008": "Biotechnology",
        "UG009": "Physics",
        "UG010": "Chemistry",
        "UG011": "Mathematics",
        "UG012": "Political Science",
        "UG013": "Sociology",
        "UG014": "Environmental Science",
        "UG015": "Media and Communication",
        "UG016": "Fine Arts",
        "UG017": "History",
        "UG018": "Philosophy",
        "UG019": "Nursing",
        "UG020": "Architecture",  
    },
    # Postgraduate Courses
    "Postgraduate":{
        "PG001": "Master of Business Administration",
        "PG002": "Master of Computer Science",
        "PG003": "Master of Mechanical Engineering",
        "PG004": "Master of Electrical Engineering",
        "PG005": "Master of Civil Engineering",
        "PG006": "Master of Data Science",
        "PG007": "Master of Biotechnology",
        "PG008": "Master of Artificial Intelligence",
        "PG009": "Master of Psychology",
        "PG010": "Master of Public Administration",
        "PG011": "Master of Economics",
        "PG012": "Master of International Relations",
        "PG013": "Master of Environmental Management",
        "PG014": "Master of Journalism",
        "PG015": "Master of Fine Arts"   
    }
}


def printAllUndergradCourses():
    courses = Courses["Undergraduate"].items()
    courses = list(courses)  # Convert to list for indexing
    max_key_length = max(len(key) for key, _ in courses)
    max_value_length = max(len(value) for _, value in courses)
    column_width = max_key_length + max_value_length + 5  # Addition of padding
    
    tripletCount = 0
    currentTriplet = ""
    
    for course_key, course_name in courses:
        if tripletCount == 3:  # Resetting point in order to have only 3 courses per row
            print(currentTriplet.strip())
            currentTriplet = ""
            tripletCount = 0
        
        if tripletCount < 3:
            currentTriplet += f"{course_key} - {course_name:<{column_width}}"
            tripletCount += 1
    
    if currentTriplet.strip():
        print(currentTriplet.strip())  # Print remaining courses that could be remaining if total courses not divisible by 3
        
        
def printAllPostgradCourses():
    courses = Courses["Postgraduate"].items()
    courses = list(courses)  # Convert to list for indexing
    max_key_length = max(len(key) for key, _ in courses)
    max_value_length = max(len(value) for _, value in courses)
    column_width = max_key_length + max_value_length + 5  # Addition of padding
    
    tripletCount = 0
    currentTriplet = ""
    
    for course_key, course_name in courses:
        if tripletCount == 3:  # Resetting point in order to have only 3 courses per row
            print(currentTriplet.strip())
            currentTriplet = ""
            tripletCount = 0
        
        if tripletCount < 3:
            currentTriplet += f"{course_key} - {course_name:<{column_width}}"
            tripletCount += 1
    
    if currentTriplet.strip():
        print(currentTriplet.strip())  # Print remaining courses that could be remaining if total courses not divisible by 3


        