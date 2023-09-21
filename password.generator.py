import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ""
    special_chars = '!@#$%^&*()_+[]{}|;:,.<>?'
    
    # Create a pool of characters based on complexity requirements
    characters = lowercase_letters + uppercase_letters
    if include_digits:
        characters += digits
    if include_special_chars:
        characters += special_chars

    # Ensure password length is not less than 4
    length = max(length, 4)

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage:
password = generate_password(length=12, include_digits=True, include_special_chars=True)
print("Generated Password:", password)
