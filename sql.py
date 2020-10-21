import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port


server = 'tcp:xxx.database.windows.net'
database = ''
username = ''
password = ''


#Azure AD Interactive, sobe a tela ABI para logar.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';Authentication=ActiveDirectoryInteractive')

#Azure AD Password, nao abre a tela para loga automatica com a variavel password
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+';Authentication=ActiveDirectoryPassword')

#Usando Autenticacao normal do SQL Server sem usar Azure AD
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()



#MYSQL Conexao Simples
#import mysql.connector
#*** para uso em container com MYSQL colocar o IP do container com MYSQL nao funciona colocando 127.0.0.1, apenas se for na maquina local e nao em um container separado.
#cnx = mysql.connector.connect(user='root', password='xxxx', host='172.17.0.2', database='mysql')
#cnx.close()


#OTHER SAMPLE WITH QUERY
'''
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='xxx', database='xxx')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()
'''
