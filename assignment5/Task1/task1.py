# Create a dictionary of student names and their marks
students = {
    "Raj": 85,
    "kumar": 90,
    "suraj": 78,
    "anand": 92
}

#  Ask the user to input a student's name
name = input("Enter the student's name: ")

#  Retrieve and display marks or show an appropriate message
if name in students:
    print(f"{name}'s marks are: {students[name]}")
else:
    print("Student not found in the record.")
