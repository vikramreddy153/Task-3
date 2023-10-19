import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        length = 8
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("-------------------Password Generator------------------")
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
