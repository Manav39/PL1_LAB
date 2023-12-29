from tkinter import *
import sqlite3

conn = sqlite3.connect("test.db")
def add_to_database():
    if student_name.get() == "" or student_age.get() == "" or student_semester.get() == "" or student_branch.get() == "":
        status.set("Please Enter all details")
    else:
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS Student(
                    name NVARCHAR PRIMARY KEY,
                    age INTEGER NOT NULL,
                    sem INTEGER NOT NULL,
                    branch NVARCHAR NOT NULL
                )
            ''')
            conn.execute(f'''
                INSERT INTO Student values('{student_name.get()}', {student_age.get()}, {student_semester.get()}, '{student_branch.get()}')
            ''')
            print("Inserted successfully")
            status.set("VALUES INSERTED SUCCESSFULLY")
            conn.commit()
        except Exception as e:
            print(e)
        
def display_records():
    cursor = conn.execute('''
        SELECT * FROM Student
    ''')
    for data in cursor:
        print(data)

win = Tk()
win.geometry("500x500")
win.resizable(0, 0)

student_name = StringVar()
student_age = StringVar()
student_semester = StringVar()
student_branch = StringVar()
status = StringVar()

frame = Frame(win, height=500, width=450)
frame.pack()

name_label = Label(frame, text="Name: ", pady=15)
name_label.grid(row=0, column=0)
name_txt = Entry(frame, width=40,textvariable=student_name)
name_txt.grid(row=0, column=1)

age_label = Label(frame, text="Age: ", pady=15)
age_label.grid(row=1, column=0)
age_txt = Entry(frame, width=40,textvariable=student_age)
age_txt.grid(row=1, column=1)

semester_label = Label(frame, text="Semester: ", pady=15)
semester_label.grid(row=2, column=0)
semester_txt = Entry(frame, width=40,textvariable=student_semester)
semester_txt.grid(row=2, column=1)

branch_label = Label(frame, text="Branch: ", pady=15)
branch_label.grid(row=3, column=0)
branch_txt = Entry(frame, width=40,textvariable=student_branch)
branch_txt.grid(row=3, column=1)

insert_button = Button(frame, text="Enter", width=20, pady=15, command=add_to_database)
insert_button.grid(row=4, column=1)

display_button = Button(frame, text="Display", width=20, pady=15, command=display_records)
display_button.grid(row=4, column=0)

status_label = Label(frame, textvariable=status, pady=15)
status_label.grid(row=5, column=0, columnspan=2)

win.mainloop()

conn.close()