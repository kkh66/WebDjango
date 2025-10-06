
def check_password_case(password):
    # Check if password has at least one uppercase letter
    has_uppercase = any(char.isupper() for char in password)

    # Check if password has at least one lowercase letter
    has_lowercase = any(char.islower() for char in password)

    # Return True if both uppercase and lowercase are present
    return has_uppercase and has_lowercase


def check_password_numeric_and_symbols(password):
    # Check if password has at least one numeric character
    has_numeric = any(char.isdigit() for char in password)

    # Check if password has at least one special symbol
    has_symbols = any(not char.isalnum() for char in password)

    # Return True if both numeric and symbols are present
    return has_numeric and has_symbols