"""
12. Create a login page backend to ask users to enter the username
and password. Make sure to ask for a Re-Type Password and if the
password is incorrect give a chance to enter it again but it should
not be more than 3 times.
"""

def register_user():
    user_name = input("Please enter your username: ")
    while True:
        password = input("Please enter a password: ")
        reenter_password = input("Re-enter your password: ")
        if password == reenter_password:
            print("Registration successful! Please login!")
            return user_name, password
        else:
            print("Passwords do not match! Try again!")

def login_user(user_name, correct_password):
    attempts = 3
    while attempts > 0:
        entered_username = input("Please enter your username: ")
        entered_password = input("Please enter your password: ")
        if entered_username == user_name and entered_password == correct_password:
            print("Login successful!")
            return True
        else:
            attempts -= 1
            print(f"Incorrect username or password! Attempts left {attempts}")

    print("Login unsuccessful. Access Denied!")
    return False

user, passw = register_user()
login_user(user, passw)
