import os

def validate_user(username, password):
    stored_user = os.getenv('USERNAME')
    stored_password = os.getenv('PASSWORD')
    return stored_user == username and stored_password == password
    

user_input = input("Nome de usuário: ")
password_input = input("Insira a senha: ")

if validate_user(user_input, password_input):
    print("Acesso confirmado.")
else:
    print("Acesso negado.")    