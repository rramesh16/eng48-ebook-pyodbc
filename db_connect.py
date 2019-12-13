import pyodbc

# Variables to connect
server = 'localhost,1433'
database = 'Ebooks'
username = 'SA'
password = 'Passw0rd2018'

# Making the connection
docker_Ebooks = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                  +server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Making the cursor
cursor = docker_Ebooks.cursor()
