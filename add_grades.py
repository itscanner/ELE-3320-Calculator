import json

def add_quiz(grade):
    """
    Add a quiz grade to the `grades.json` file under the 'Quizzes' section, and update the count of 'S' and 'NY' grades.
    param quiz_grade: The grade of the quiz, 'S' = Satisfactory, 'NY' = Not Yet
    returns: True if the quiz was added successfully, False otherwise
    """
    if grade not in ['S', 'NY']:
        return False
    
    # get current grades data
    try:
        with open('grades.json', 'r') as file:
            grades_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        grades_data = {'quizzes': {'S': 0, 'NY': 0}}
    
    if 'quizzes' not in grades_data:
        grades_data['quizzes'] = {'S': 0, 'NY': 0}
    
    grades_data['quizzes'][grade] += 1
    
    # write the updated grades data back to the file
    with open('grades.json', 'w') as file:
        json.dump(grades_data, file, indent=4)
        
    return True

def add_matlab_lab(grade):
    """
    Add a grade to the `grades.json` file under the 'MATLAB Labs' section.
    param grade: The grade of the MATLAB lab, 'S' = Satisfactory, 'NY' = Not Yet
    returns: True if the grade was added successfully, False otherwise
    """
    if grade not in ['S', 'NY']:
        return False
    
    # get current grades data
    try:
        with open('grades.json', 'r') as file:
            grades_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        grades_data = {'matlab': {}}

    if 'matlab' not in grades_data:
        grades_data['matlab'] = {'S': 0, 'NY': 0}

    grades_data['matlab'][grade] += 1

    # write the updated grades data back to the file
    with open('grades.json', 'w') as file:
        json.dump(grades_data, file, indent=4)
    
    return True

def add_rtdsp_lab(grade):
    """
    Add a grade to the `grades.json` file under the 'RTDSP Labs' section.
    param grade: The grade of the RTDSP lab, 'E' = Exemplary, 'M' = Meets Expectations, 'P' = Progressing, 'X' = Incomplete
    returns: True if the grade was added successfully, False otherwise
    """
    if grade not in ['E', 'M', 'P', 'X']:
        return False
    
    # get current grades data
    try:
        with open('grades.json', 'r') as file:
            grades_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        grades_data = {'rtdsp': {}}

    if 'rtdsp' not in grades_data:
        grades_data['rtdsp'] = {'E': 0, 'M': 0, 'P': 0, 'X': 0}

    grades_data['rtdsp'][grade] += 1

    # write the updated grades data back to the file
    with open('grades.json', 'w') as file:
        json.dump(grades_data, file, indent=4)
    
    return True

def add_exam_questions(total_count, grade):
    """Adds the total_count of exam questions with the given grade to the `grades.json` file under the 'Exam Questions' section.
    param total_count: The total number of exam questions with the given grade
    param grade: The grade of the exam questions, 'E' = Exemplary, 'M' = Meets Expectations, 'P' = Progressing, 'X' = Incomplete
    returns: True if the exam questions were added successfully, False otherwise
    """
    if grade not in ['E', 'M', 'P', 'X']:
        return False
    
    # get current grades data
    try:
        with open('grades.json', 'r') as file:
            grades_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        grades_data = {'exams': {}}

    if 'exams' not in grades_data:
        grades_data['exams'] = {'E': 0, 'M': 0, 'P': 0, 'X': 0}

    grades_data['exams'][grade] += total_count

    # write the updated grades data back to the file
    with open('grades.json', 'w') as file:
        json.dump(grades_data, file, indent=4)
    
    return True
