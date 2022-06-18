from tkinter import*
import sqlite3
from tkinter import messagebox

root = Tk()
root.title("Facebook")
root.iconbitmap("logo.ico")


conn = sqlite3.connect('facebook.db')

c = conn.cursor()

def submit():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES (:f_name, :l_name, :address, :age, :password, :father_name, :city, :zip_code)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'age':age.get(),
        'password':password.get(),
        'father_name':father_name.get(),
        'city':city.get(),
        'zip_code':zip_code.get()
    })

    messagebox.showinfo("User", "Inserted Successfully")
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    age.delete(0,END)
    password.delete(0,END)
    father_name.delete(0,END)
    city.delete(0,END)
    zip_code.delete(0,END)

def query():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM user")
    records = c.fetchall()
    print(records)

    print_record=' '
    for record in records:
        print_record +=str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[7]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=10, column=0, columnspan=2)
     
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    c.execute("DELETE from user WHERE oid = " + delete_box.get())
    c.execute("SELECT *, oid FROM user")

    records =   c.fetchall()

    print_record = ''
    for record in records:
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"
    query_label = Label(root, text=print_record)
    query_label.grid(row=10, column=0, columnspan=2)

    print("deleted sucefully")

    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute(""" UPDATE user SET
        first_name = :first,
        last_name = :last,
        address = :address,
        age = :age,
        password = :password,
        father_name = :father_name,
        city = :city,
        zip_code = :zip_code
        WHERE oid = :oid""",
        {'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'address': address_editor.get(),
        'age': age_editor.get(),
        'password': password_editor.get(),
        'father_name': father_name_editor.get(),
        'city': city_editor.get(),
        'zip_code': zip_code_editor.get(),
        'oid': record_id
        }
    )
    
    conn.commit()
    conn.close()
    editor.destroy()

def edit():
    global editor
    editor = Toplevel()
    editor.title("Update Data")
    editor.geometry('300x300')
    conn = sqlite3.connect('facebook.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM user WHERE oid=" + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global age_editor
    global password_editor
    global father_name_editor
    global city_editor
    global zip_code_editor
    
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    
    age_editor = Entry(editor, width=30)
    age_editor.grid(row=3, column=1)

    password_editor = Entry(editor, width=30)
    password_editor.grid(row=4, column=1)
    
    father_name_editor = Entry(editor, width=30)
    father_name_editor.grid(row=5, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=6, column=1)

    zip_code_editor = Entry(editor, width=30)
    zip_code_editor.grid(row=7, column=1)
    
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10,0))
    
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)

    age_label = Label(editor, text="Age")
    age_label.grid(row=3, column=0)
    
    password_label = Label(editor, text="Password")
    password_label.grid(row=4, column=0)

    father_name_label = Label(editor, text="Father Name")
    father_name_label.grid(row=5, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=6, column=0)

    zipcode_label = Label(editor, text="Zip Code")
    zipcode_label.grid(row=7, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        age_editor.insert(0, record[3])
        password_editor.insert(0, record[4])
        father_name_editor.insert(0, record[5])
        city_editor.insert(0, record[6])
        zip_code_editor.insert(0, record[7])

    edit_btn = Button(editor, text="Save", command=update)
    edit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1 ,padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

age = Entry(root, width=30)
age.grid(row=3, column=1)

password = Entry(root,show="*", width=30)
password.grid(row=4, column=1)

father_name = Entry(root, width=30)
father_name.grid(row=5, column=1)

city = Entry(root, width=30)
city.grid(row=6, column=1)

zip_code = Entry(root, width=30)
zip_code.grid(row=7, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=11, column=1, pady=5)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

age_label = Label(root, text="Age")
age_label.grid(row=3, column=0)

password_label = Label(root, text="Password")
password_label.grid(row=4, column=0)

father_name_label = Label(root, text="Father Name")
father_name_label.grid(row=5, column=0)

city_label = Label(root, text="City")
city_label.grid(row=6, column=0)

zip_code_label = Label(root, text="Zip Code")
zip_code_label.grid(row=7, column=0)

delete_box_label = Label(root, text="Delete ID")
delete_box_label.grid(row=11, column=0, pady=5)

submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

edit_btn = Button(root, text="Update", command=edit)
edit_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=120)

conn.commit()
conn.close()

root.mainloop()