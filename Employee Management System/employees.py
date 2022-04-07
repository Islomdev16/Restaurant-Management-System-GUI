from tkinter import *
from tkinter import ttk
from databases import Database

db = Database('Employee.db')
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.resizable(False, False)
root.config(bg="#2c3e50")
# root.attributes('-zoomed')

name = StringVar()
surname = StringVar()
age = StringVar()
role = StringVar()
joined_date = StringVar()
email = StringVar()
gender = StringVar()
country = StringVar()
phone_number = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 21, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Calibri", 16), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblSurname = Label(entries_frame, text="Surname", font=("Calibri", 16), bg="#535c68", fg="white")
lblSurname.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtSurname = Entry(entries_frame, textvariable=surname, font=("Calibri", 16), width=30)
txtSurname.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
lblAge.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
txtAge.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lblRole = Label(entries_frame, text="Role of employee(s)", font=("Calibri", 16), bg="#535c68", fg="white")
lblRole.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtRole = Entry(entries_frame, textvariable=role, font=("Calibri", 16), width=30)
txtRole.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblJoined_date = Label(entries_frame, text="Joined Date", font=("Calibri", 16), bg="#535c68", fg="white")
lblJoined_date.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtJoined_date = Entry(entries_frame, textvariable=joined_date, font=("Calibri", 16), width=30)
txtJoined_date.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=3, column=3, padx=10, pady=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
lblGender.grid(row=1, column=5, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=29, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=1, column=6, padx=10, sticky="w")

lblCountry = Label(entries_frame, text="Country", font=("Calibri", 16), bg="#535c68", fg="white")
lblCountry.grid(row=2, column=5, padx=10, pady=10, sticky="w")
txtCountry = Entry(entries_frame, textvariable=country, font=("Calibri", 16), width=30)
txtCountry.grid(row=2, column=6, padx=10, pady=10, sticky="w")

lblPhone_number = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
lblPhone_number.grid(row=3, column=5, padx=10, pady=10, sticky="w")
txtPhone_number = Entry(entries_frame, textvariable=phone_number, font=("Calibri", 16), width=30)
txtPhone_number.grid(row=3, column=6, padx=10, pady=10, sticky="w")

lblAddress = Label(entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
lblAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtAddress = Text(entries_frame, font=("Calibri", 16), width=90, height=6)
txtAddress.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

# Buttons Section
def displayAll():
    for row in db.fetch():
        tv.insert("", END, values=row)

def add_employee():
    pass

def update_employee():
    pass

def delete_employee():
    pass

def clearAll():
    pass
    # name.set("")
    # surname.set("")
    # age.set("")
    # role.set("")
    # joined_date.set("")
    # email.set()
    # gender.set("")
    # country.set("")
    # phone_number.set("")
    # txtAddress.set(1.0)


btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#16a085", bd=0).grid(row=0, column=0)

Button(btn_frame, command=update_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#2980b9", bd=0).grid(row=0, column=1, padx=10)

Button(btn_frame, command=delete_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#c0392b", bd=0).grid(row=0, column=2, padx=10)

Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)

# Table Frame Section
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=500, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=("Calibri", 18), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=("Calibri", 13))

tv = ttk.Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8,9,10,11), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=1)
tv.heading("2", text="Name")
tv.column("2", width=80)
tv.heading("3", text="Surname")
tv.column("3", width=100)
tv.heading("4", text="Age")
tv.column("4", width=10)
tv.heading("5", text="Role")
tv.column("5", width=180)
tv.heading("6", text="Joined Date")
tv.column("6", width=80)
tv.heading("7", text="Email")
tv.heading("8", text="Gender")
tv.column("8", width=35)
tv.heading("9", text="Country")
tv.column("9", width=110)
tv.heading("10", text="Contact No")
tv.column("10", width=130)
tv.heading("11", text="Address NO")
tv.column("11", width=360)
tv["show"] = 'headings'
tv.pack(fill=X)


displayAll()
root.mainloop()
