import sqlite3
conn = sqlite3.connect("insta.db")
cur = conn.cursor()




sql = """ CREATE TABLE users(
    name TEXT(30)  NOT NULL,
    username VARCHAR(30) NOT NULL,
    email_id VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(8) NOT NULL UNIQUE,
    dob DATE NULL 
) """


cur.execute(sql)
print("MADE MODIFICATION")




conn.commit()
conn.close()




""" ALTER TABLE INSTA_USER
ADD CONSTRAINT CK_INSTA_USER CHECK(email_id LIKE '%@%.%')
"""

"""MODIFY TABLE INSTA_USER
ADD CONSTRAINT CK_INSTA_USER CHECK(password LIKE '%[^a-zA-Z0-9]%')
"""