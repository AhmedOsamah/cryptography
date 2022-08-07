import sqlite3
dbase = sqlite3.connect('data.db')
cursor = dbase.cursor()
def add(name,email,password):
    cursor.execute('''INSERT INTO users values(?,?,?)''',(name,email,password))
    dbase.commit()
def check(name,password):
    data = cursor.execute('''Select UserName,password from users''')
    for d in data:
        if(name == str(d[0]) and password==str(d[1])):
            return True

