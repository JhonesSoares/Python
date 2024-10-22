import json
import os

# Função para carregar dados do arquivo JSON
def load_data(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r') as file_jason:
            try:
                return json.load(file_jason)  # Carrega os dados existentes
            except json.JSONDecodeError:
                return []  # Retorna uma lista vazia se o arquivo estiver vazio ou corrompido
    return []  # Retorna uma lista vazia se o arquivo não existir

# Função para salvar dados no arquivo JSON
def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf8') as file_jason:
        json.dump(data, file_jason, indent=4)

# Função para adicionar novo dado
def add_data(file_path, new_datas):
    dates_exist = load_data(file_path)  # Carrega os dados existentes
    dates_exist.append(new_datas)  # Adiciona o novo dado
    save_data(file_path, dates_exist)  # Salva os dados atualizados



# Exemplo de uso
#file_path = 'banco_dados.json'
CAMINHO_ARQUIVO = 'C:\\Users\\jhone\\OneDrive\\Documentos\\GitHub\\Python\\Python Udemy\\Intermediário\\lista_de_tarefas\\listadetarefas.json'
# Novo dado a ser adicionado
#new_datas = {
#    'id': 1,
#    'nome': 'João',
#    'idade': 25
#}

if __name__=='__main__':
    # Adicionar o novo dado ao banco de dados JSON
    #add_data(file_path, new_datas)
    ...
