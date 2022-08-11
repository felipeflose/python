
import sqlite3

class Sql():
    def conexao():
        caminhoBD = '\\\\desktop-73e3j72\\bd\\'
        nomeTable = 'internet.db'
        con = sqlite3.connect(caminhoBD+nomeTable)
        return con
    def cria_table():
        caminhoBD = '\\\\desktop-73e3j72\\bd\\'
        nomeTable = 'internet.db'
        sql_create = 'create table teste '\
                     '(idExec INTEGER primary key AUTOINCREMENT, '\
                     'dt_teste date, '\
                     'hora_teste time, '\
                     'hora_fechada int, '\
                     'down int, '\
                     'chegou int, '\
                     'up int, '\
                     'dtProcesso date, '\
                     'hrProcesso time) '            
        #os.remove(caminhoBD+nomeTable) if os.path.exists(caminhoBD+nomeTable) else 
        Sql.exec(sql_create)
    def cursor():
        cur = Sql.conexao().cursor()
        return cur
    def exec(x):
        cur = Sql.conexao().cursor().execute(x)
        return cur  


#Sql.cria_table()


sql_select = 'select * from teste'

Sql.exec(sql_select)
dados = Sql.cursor().fetchall()
print(dados)

for linha in dados:
    print (linha)