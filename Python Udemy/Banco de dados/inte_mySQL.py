#INSTALE A BIBLIOTECA ( !pip install mysql-connector-python )

#import a biblioteca
import mysql.connector as mysql

#defina os prarânmetros de conexão
mysql = mysql.connect(
    host = 'endereco IP ou nome do servidor', 
    port = '5432', 
    database = 'nome do banco de dados', 
    user = 'usuario', 
    password = 'senha')

#CRIE CURSOR
mysql_cursor = mysql.cursor()

#USE CURSOR PARA EXECUTAR COMANDOS SQL
mysql_cursor.execute('seu comando SQL aqui')