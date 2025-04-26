def is_valid(username, password):
    # Write your code below
    if username == "admin":
        return True
    elif username== "user" and password == "qweasd":
        return True
    else:
        return False

usr_name = input()
password = input()
# Call the function below
result = is_valid(usr_name, password)
print(result)