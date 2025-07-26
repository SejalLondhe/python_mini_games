from cryptography.fernet import Fernet
import os

# Run this only once to generate the key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    """Load the secret key from key.key file"""
    with open("key.key", "rb") as file:
        return file.read()

key = load_key()
fer = Fernet(key)

def view_passwords():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return

    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if "|" not in data:
                continue
            user, encrypted_pwd = data.split("|")
            decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
            print(f"Account: {user} | Password: {decrypted_pwd}")

def add_password():
    name = input('Enter account name: ')
    pwd = input('Enter password: ')
    with open('passwords.txt', 'a') as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pwd + "\n")
    print("Password added successfully.")

def clear_passwords():
    if not os.path.exists("passwords.txt"):
        print("No passwords to clear.")
        return

    confirm = input("Are you sure you want to delete all saved passwords? (yes/no): ").lower()
    if confirm == "yes":
        open("passwords.txt", "w").close()
        print("All passwords have been cleared.")
    else:
        print("Clear operation canceled.")

while True:
    mode = input("\nChoose an option (add/view/clear), or 'q' to quit: ").lower()

    if mode == "q":
        break
    elif mode == "add":
        add_password()
    elif mode == "view":
        view_passwords()
    elif mode == "clear":
        clear_passwords()
    else:
        print("Invalid option. Please choose 'add', 'view', 'clear', or 'q'.")
