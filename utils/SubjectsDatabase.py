# Rudimentary python database for undergraduate courses and postgraduate courses #

Courses = {
    # Undergraduate Courses
    "Undergraduate":{
        "UG-001": "Computer Science",
        "UG-002": "Mechanical Engineering",
        "UG-003": "Electrical Engineering",
        "UG-004": "Civil Engineering",
        "UG-005": "Business Administration",
        "UG-006": "Psychology",
        "UG-007": "Economics",
        "UG-008": "Biotechnology",
        "UG-009": "Physics",
        "UG-010": "Chemistry",
        "UG-011": "Mathematics",
        "UG-012": "Political Science",
        "UG-013": "Sociology",
        "UG-014": "Environmental Science",
        "UG-015": "Media and Communication",
        "UG-016": "Fine Arts",
        "UG-017": "History",
        "UG-018": "Philosophy",
        "UG-019": "Nursing",
        "UG-020": "Architecture",  
    },
    # Postgraduate Courses
    "Postgraduate":{
        "PG-001": "Master of Business Administration",
        "PG-002": "Master of Computer Science",
        "PG-003": "Master of Mechanical Engineering",
        "PG-004": "Master of Electrical Engineering",
        "PG-005": "Master of Civil Engineering",
        "PG-006": "Master of Data Science",
        "PG-007": "Master of Biotechnology",
        "PG-008": "Master of Artificial Intelligence",
        "PG-009": "Master of Psychology",
        "PG-010": "Master of Public Administration",
        "PG-011": "Master of Economics",
        "PG-012": "Master of International Relations",
        "PG-013": "Master of Environmental Management",
        "PG-014": "Master of Journalism",
        "PG-015": "Master of Fine Arts"   
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


        