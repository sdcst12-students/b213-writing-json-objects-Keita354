#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""

import json

class TeacherData:
    def __init__(self):
        self.assignments = []

    def create_assignment(self, assignment_name, assignment_value):
        assignment_id = len(self.assignments)
        assignment = {'id': assignment_id, 'name': assignment_name, 'value': assignment_value, 'scores': {}}
        self.assignments.append(assignment)
        print(f"Your assignment has been assigned ID {assignment_id}")

    def enter_scores(self, assignment_id):
        if 0 <= assignment_id < len(self.assignments):
            assignment = self.assignments[assignment_id]
            print(f"Enter in the scores for {len(assignment['scores']) + 1} students for {assignment['name']}:")
            student_id = 1
            while True:
                try:
                    score = float(input(f"{student_id}: _"))
                    assignment['scores'][student_id] = score
                    student_id += 1
                except ValueError:
                    print("Invalid input. Please enter a valid score.")
                if student_id > 10:
                    break
            print("Complete.")
        else:
            print("Invalid assignment ID. Please enter a valid assignment ID.")

    def write_to_file(self):
        with open('teacher_data.json', 'w') as file:
            json.dump(self.assignments, file, indent=2)
        print("Data has been written to file.")

def main():
    teacher_data = TeacherData()

    while True:
        print("\n1. Create an Assignment\n2. Enter in Assignment Scores\n3. Write your data to file")
        choice = input("\nEnter in your choice: _")

        if choice == '1':
            assignment_name = input("Enter the assignment name: _")
            assignment_value = float(input("Enter in Assignment Value: _"))
            teacher_data.create_assignment(assignment_name, assignment_value)
        elif choice == '2':
            assignment_id_input = input("Enter in the assignment ID: _")
            try:
                assignment_id = int(assignment_id_input)
                teacher_data.enter_scores(assignment_id)
            except ValueError:
                print("Invalid input. Please enter a valid assignment ID.")
        elif choice == '3':
            teacher_data.write_to_file()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
