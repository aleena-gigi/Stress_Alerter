import sqlite3 as sq
conn=sq.connect('test.db')
conn.execute('''CREATE TABLE USERINFO
                (UNAME VARCHAR(30) NOT NULL,
                PSWD VARCHAR(30) NOT NULL,
                EMAIL VARCHAR(30) PRIMARY KEY NOT NULL
                );''')
print("database created successfully")