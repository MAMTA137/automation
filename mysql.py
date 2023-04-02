import sqlite3
conn = sqlite3.connect("insta.db")
cur = conn.cursor()




sql = """
CREATE TABLE INSTA_USER(
    
    name TEXT(30)  NOT NULL,
    username VARCHAR(30) NOT NULL PRIMARY KEY,
    email_id VARCHAR(254) NOT NULL,
    password VARCHAR(12) NOT NULL,
    dob DATE NULL 
    
)
"""
cur.execute(sql)
print("data has been recorded successfully")

conn.commit()
conn.close()
