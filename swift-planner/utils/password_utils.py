# utils/password_utils.py

import random
import string

def generate_password(length=12):
    if length < 6:
        raise ValueError("Password must be at least 6 characters.")
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password



# Example usage
if __name__ == "__main__":
    print("Generated password:", generate_password())
