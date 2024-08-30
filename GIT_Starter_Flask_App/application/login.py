# name = input("Username:")
#
# while name == "":
#     print("You did not enter your username")
#     name = input("Username:")
#
#
# print(f"Hello {name}")


import re


def is_strong_password(password):
    """Check if the password is strong."""
    # Minimum 8 characters
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # At least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."

    # At least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."

    # At least one digit
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."

    # At least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."

    return True, "Password is strong."

def get_username_and_password():
    """Prompt user for username and password."""
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the password is strong
    is_strong, feedback = is_strong_password(password)

    if is_strong:
        print(f"Welcome, {username}! Your password is strong.")
    else:
        print(f"Password is not strong enough: {feedback}")

if __name__ == "__main__":
    get_username_and_password()
