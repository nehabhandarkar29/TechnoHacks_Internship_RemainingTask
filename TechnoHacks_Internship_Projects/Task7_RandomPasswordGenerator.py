import random
import string

def generate_random_password(length):
    """Function to generate a random password of specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter the length of the password: "))

    if length <= 0:
        print("Invalid password length.")
    else:
        password = generate_random_password(length)
        print("Your random password is:", password)

if __name__ == "__main__":
    main()
