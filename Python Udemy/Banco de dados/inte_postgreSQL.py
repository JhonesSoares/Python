#INSTALE A BIBLIOTECA ( !pip install psycopg2 )

#import a biblioteca
import psycopg2

#defina os prarânmetros de conexão
pgsql = psycopg2.connect(
    host = 'endereco IP ou nome do servidor', 
    port = '5432', 
    database = 'nome do banco de dados', 
    user = 'usuario', 
    password = 'senha')

#CRIE CURSOR
pgsql_cursor = pgsql.cursor()

#USE CURSOR PARA EXECUTAR COMANDOS SQL
pgsql_cursor.execute('seu comando SQL aqui')