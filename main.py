def create_student_dict(name, age, major):
    # Write code here
    student = {
        "name": name,
        "age": age,
        "major": major
    }
    return student

name = input()
age = int(input())
major = input()
print(create_student_dict(name, age, major))