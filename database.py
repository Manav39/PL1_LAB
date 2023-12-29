import sqlite3

conn = sqlite3.connect("Student.db")

# conn.execute('''
#         CREATE TABLE DEPARTMENT(
#             Code INTEGER KEY NOT NULL,
#             Branch VARCHAR NOT NULL,
#             StudentCount INTEGER NOT NULL
#         );
# ''')

# conn.commit()
# print("Department Table Created")

# conn.execute('''
#         CREATE TABLE STUDENTS(
#             Branch INTEGER NOT NULL,
#             ID INTEGER NOT NULL,
#             Name VARCHAR NOT NULL,
#             LastName VARCHAR NOT NULL,
#             CONSTRAINT fk_department_code FOREIGN KEY(Branch) REFERENCES DEPARTMENT(Code)
#         );
# ''')
# conn.commit();
# print("Studnets Table Created")

# conn.execute('''INSERT INTO DEPARTMENT VALUES(02,'IT',12)''')
# conn.execute('''INSERT INTO DEPARTMENT VALUES(03,'EXTC',15)''')
# conn.execute('''INSERT INTO DEPARTMENT VALUES(04,'TE',16)''')

# data = conn.execute("SELECT * FROM DEPARTMENT")
# for row in data:
#     print(row)

# conn.execute('''INSERT INTO STUDENTS VALUES(03,103,'Ram','Qureshi')''')
# conn.execute('''INSERT INTO STUDENTS VALUES(04,104,'Bhupendar','Jogi')''')
# conn.execute('''INSERT INTO STUDENTS VALUES(02,105,'Man','Menta')''')
# conn.commit()
# print("Added")

# data = conn.execute("SELECT * FROM STUDENTS")
# for row in data:
#     print(row)

