import json

def carregar_dados():
    with open('usuarios.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def validar_login(usuario, senha):
    dados = carregar_dados()
    for usuario_cadastrado in dados['usuarios']:
        if usuario_cadastrado['usuario'] == usuario and usuario_cadastrado['senha'] == senha:
            return True
    return False

def main():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
    if validar_login(usuario, senha):
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

if __name__ == "__main__":
    main()