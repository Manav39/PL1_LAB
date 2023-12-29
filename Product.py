from tkinter import *
import sqlite3

conn = sqlite3.connect("Prod.db")

def add_to_database():
    if product_name.get() == "" or quantity.get() == "" or details.get()=="" or price.get() == "" or pid.get() == "":
        status.set("Please Enter All Details")
    else:
        try:
            conn.execute('''
                    CREATE TABLE IF NOT EXISTS Product(
                    name VARCHAR NOT NULL,
                    quanity INTEGER NOT NULL,
                    details VARCHAR NOT NULL,
                    price INTEGER NOT NULL,
                    pid VARCHAR KEY NOT NULL
                 )
            ''')
            conn.execute(f'''
                INSERT INTO Product VALUES('{product_name.get()}',{quantity.get()},'{details.get()}',{price.get()},'{pid.get()}')
            ''')
            conn.commit()
            status.set("Product Added Succesfully")
        except Exception as e:
            print(e)
            status.set(e)

def display_records():
    data = conn.execute('''SELECT * FROM Product''')
    for row in data:
        print(row)

def edit_prod():
    try:
        conn.execute(f'''
        UPDATE Product SET name='{product_name.get()}',quanity={quantity.get()},details='{details.get()}',price={price.get()}
        WHERE pid='{pid.get()}'
        ''')
        conn.commit()
    except Exception as e:
        status.set(e)

def del_product():
    try:
        conn.execute(f'''
            DELETE FROM Product where pid = '{delprod.get()}'
        ''')
        status.set("Product Deletd Successfully")
    except Exception as e:
        status.set(e)

win = Tk()
win.geometry("550x500")
win.resizable(0,0)

frame = Frame(win,height=500,width=400)
frame.pack()

product_name = StringVar()
quantity = StringVar()
details = StringVar()
price = StringVar()
pid=StringVar()
status =StringVar()
delprod = StringVar()

prod_name = Label(frame,text="Enter Product Name : ",pady=15)
prod_name.grid(row = 0,column = 0)
prod_input = Entry(frame,width=50,textvariable=product_name)
prod_input.grid(row = 0,column=1)

prod_quantity = Label(frame,text="Enter Product quantity : ",pady=15)
prod_quantity.grid(row = 1,column = 0)
quan_input = Entry(frame,width=50,textvariable=quantity)
quan_input.grid(row = 1,column=1)

prod_details = Label(frame,text="Enter Product details : ",pady=15)
prod_details.grid(row = 2,column = 0)
details_input = Entry(frame,width=50,textvariable=details)
details_input.grid(row = 2,column=1)

prod_price = Label(frame,text="Enter Product price : ",pady=15)
prod_price.grid(row = 3,column = 0)
price_input = Entry(frame,width=50,textvariable=price)
price_input.grid(row = 3,column=1)

prod_id = Label(frame,text="Enter Product ID : ",pady=15)
prod_id.grid(row = 4,column = 0)
id_input = Entry(frame,width=50,textvariable=pid)
id_input.grid(row = 4,column=1)

add_btn = Button(frame,text="Add Product",padx=5,pady=5,command=add_to_database)
add_btn.grid(row=6,column=0)

display_btn = Button(frame,text="Display Products",padx=5,pady=5,command=display_records)
display_btn.grid(row=6,column=1)

edit_btn = Button(frame,text="Edit Product",padx=5,pady=5,command=edit_prod)
edit_btn.grid(row=6,column=2)

status_prod = Label(frame,textvariable=status)
status_prod.grid(row = 7,column=1)

del_label = Label(frame,text="To delete a product enter PID",padx=10)
del_label.grid(row =9,column=1)

del_input = Entry(frame,textvariable=delprod)
del_input.grid(row=10,column=1)

del_btn = Button(frame,text="Delete",command=del_product)
del_btn.grid(row=11,column=1)

win.mainloop()
conn.close()