import re
import json
import hashlib

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*]", password):
        return False
    return True

def compare_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
    if hashed_password in passwords.values():
        print("This password has already been used, please use a different password.")
        return False
    return True

def add_password(username, password):
    passwords = {}
    hashed_password = None
    if not is_valid_password(password):
        print("Le mot de passe ne respecte pas les critères de sécurité.")
        return
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except json.decoder.JSONDecodeError:
        passwords = {}

    passwords[username] = hashed_password

    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def display_passwords():
    with open("passwords.json", "r") as file:
        passwords = json.load(file)

    for username, hashed_password in passwords.items():
        print(username + ": " + hashed_password)

while True:
    choice = input("Choisissez une option (ajouter/afficher/quitter): ")

    if choice == "ajouter":
        username = input("Entrez un nom d'utilisateur: ")
        password = input("Entrez un mot de passe: ")
        if compare_password(password) == False:
            break
        add_password(username, password)
    elif choice == "afficher":
        display_passwords()
    elif choice == "quitter":
        break
    else:
        print("Option non valide.")