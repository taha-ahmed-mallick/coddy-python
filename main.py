# Step 1: Create the Grades Dictionary
grades = {
    # Add initial student grades here
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
}

# Step 2: Access All Keys and Values
# Print all students and grades
print(f"Students: {grades.keys()}")
print(f"Grades: {grades.values()}")
# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] = 92
# Step 4: Retrieve a Student's Grade
# Get Bob's grade using get() method
print(f"Bob's grade: {grades.get('Bob')}")
# Step 5: Remove a Student
# Remove Charlie using pop() method
# Print the updated dictionary
grades.pop("Charlie")
print(f"Updated grades: {grades}")