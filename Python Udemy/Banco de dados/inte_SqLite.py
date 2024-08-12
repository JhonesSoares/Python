#INSTALE A BIBLIOTECA ( !pip install sqlite3 )

#import a biblioteca
import sqlite3

#defina os prarânmetros de conexão
sqlite = sqlite3.connect(
    host = 'endereco IP ou nome do servidor', 
    port = '5432', 
    database = 'nome do banco de dados', 
    user = 'usuario', 
    password = 'senha')

#CRIE CURSOR
sqlite_cursor = sqlite.cursor()

#USE CURSOR PARA EXECUTAR COMANDOS SQL
sqlite_cursor.execute('seu comando SQL aqui')