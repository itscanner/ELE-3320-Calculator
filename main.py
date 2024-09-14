import json
import os
from calculate_grade import calculate_grade
from add_grades import add_quiz, add_matlab_lab, add_rtdsp_lab, add_exam_questions

GRADES_FILE = 'grades.json'

def load_grades():
    """Load grades data from the JSON file."""
    if not os.path.exists(GRADES_FILE):
        return {}
    
    with open(GRADES_FILE, 'r') as file:
        return json.load(file)

def save_grades(data):
    """Save grades data to the JSON file."""
    with open(GRADES_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def calculate_final_grade():
    """Calculate and print the final grade based on current data."""
    grades_data = load_grades()
    
    if not grades_data:
        print("No grades data found. Please add some grades first.")
        return
    
    grade = calculate_grade(grades_data)
    print(f"Your current grade is: {grade}")

def add_quiz_grade():
    """Add a quiz grade."""
    grade = input("Enter quiz grade (S = Satisfactory, NY = Not Yet): ").strip().upper()
    
    if add_quiz(grade):
        print("Quiz grade added successfully.")
    else:
        print("Invalid quiz grade. Must be 'S' or 'NY'.")

def add_matlab_lab_grade():
    """Add a MATLAB lab grade."""
    grade = input("Enter MATLAB lab grade (S = Satisfactory, NY = Not Yet): ").strip().upper()
    
    if add_matlab_lab(grade):
        print("MATLAB lab grade added successfully.")
    else:
        print("Invalid quiz grade. Must be 'S' or 'NY'.")

def add_rtdsp_lab_grade():
    """Add an RTDSP lab grade."""
    grade = input("Enter RTDSP lab grade (E = Exemplary, M = Meets Expectations, P = Progressing, X = Incomplete): ").strip().upper()
    
    if add_rtdsp_lab(grade):
        print("RTDSP lab grade added successfully.")
    else:
        print("Invalid RTDSP lab grade. Must be 'E', 'M', 'P', or 'X'.")

def add_exam_questions_grade():
    """Add exam questions of a specific grade type."""
    total_count = input("Enter total number of exam questions: ").strip()
    grade = input("Enter exam question grade (E = Exemplary, M = Meets Expectations, P = Progressing, X = Incomplete): ").strip().upper()
    
    if total_count.isdigit() and add_exam_questions(int(total_count), grade):
        print("Exam questions added successfully.")
    else:
        print("Invalid input. Please enter a valid number and grade.")

def print_menu():
    """Print the CLI options menu."""
    print("\n--- ELE-3320 Grade Calculator---")
    print("1. Calculate Grade")
    print("2. Add Quiz Grade")
    print("3. Add MatLab Lab Grade")
    print("4. Add RTDSP Lab Grade")
    print("5. Add Exam Questions of Grade Type")
    print("6. Exit")
    print("----------------------------")

def main():
    """Main function to run the CLI tool."""
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            calculate_final_grade()
        elif choice == '2':
            add_quiz_grade()
        elif choice == '3':
            add_matlab_lab_grade()
        elif choice == '4':
            add_rtdsp_lab_grade()
        elif choice == '5':
            add_exam_questions_grade()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
