from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3




def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Costumer_Data 
                    (name TEXT, item TEXT, quantity INT, receipt INT)""")

    cursor.execute("SELECT * FROM Costumer_Data")
    results = cursor.fetchall()
    conn.commit()
    return results






def enter_data():
    # Getting Info
    name= name_entry.get()
    item = item_entry.get()
    quantity = quantity_spinbox.get()
    receipt = receipt_spinbox.get()

    print("Name: ", name)
    print("Item Hired: ", item)
    print("Quantity: ", quantity)
    print("Receipt: ", receipt)
    print("********************")


    # Create SQLite Table
    conn = sqlite3.connect('data.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS Costumer_Data 
                    (name TEXT, item TEXT, quantity INT, receipt INT)
            '''
    conn.execute(table_create_query)
            
    # Insert Data
    data_insert_query = '''INSERT INTO Costumer_Data (name, item, quantity, 
            receipt) VALUES 
            (?, ?, ?, ?)'''
    data_insert_tuple = (name, item, quantity, receipt)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    cursor.execute("SELECT * FROM Costumer_Data")
    conn.commit()
    conn.close()
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result))


def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Costumer_Data 
                    (name TEXT, item TEXT, quantity INT, receipt INT)""")

    cursor.execute("DELETE FROM Costumer_Data WHERE name = '" + str(data) + "'")
    conn.commit()



def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result))

def update (name, item, quantity, receipt):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Costumer_Data(name TEXT, item TEXT, quantity INT, receipt INT)""")

    cursor.execute("UPDATE Costumer_Data SET name = '" + str(name) + "', item = '" + str(item) + "', quantity = '" + str(quantity) + "', receipt = '" + str(receipt) + "' WHERE name='"+ str(name) +"'")
    conn.commit()
    
def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(name_entry.get(), item_entry.get(), quantity_spinbox.get(), receipt_spinbox.get(), update_name)
    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=result, text="", values=(result))
    




# Clear function
def clear():
    name_entry.delete(0, END)
    item_entry.delete(0, END)
    quantity_spinbox.delete(0, END)
    receipt_spinbox.delete(0, END)


data =[]

# Window
root = Tk()
root.title("Julie's Party Hire Store")
root.iconbitmap(r"C:\Users\namkh\OneDrive\Tài liệu\GitHub\Learning-Py\Tkinter\yohan.ico")
root.geometry("700x530")




frame = Frame(root)
frame.pack()

# Saving Costumer Details
info_frame =LabelFrame(frame, text="Costumer Information")
info_frame.grid(row= 0, column=0, padx=20, pady=10)

name_label = Label(info_frame, text=" Name")
name_label.grid(row=0, column=0)
item_label = Label(info_frame, text="Item")
item_label.grid(row=0, column=1)

name_entry = Entry(info_frame)
name_entry.grid(row=1, column=0)
item_entry = Entry(info_frame)
item_entry.grid(row=1, column=1)

quantity_label = Label(info_frame, text="Quantity")
quantity_spinbox = Spinbox(info_frame, from_=0, to=100)
quantity_label.grid(row=2, column=0)
quantity_spinbox.grid(row=3, column=0)

quantity_label = Label(info_frame, text="Quantity")
quantity_spinbox = Spinbox(info_frame, from_=0, to=100)
quantity_label.grid(row=2, column=0)
quantity_spinbox.grid(row=3, column=0)

receipt_label = Label(info_frame, text="Receipt")
receipt_spinbox = Spinbox(info_frame, from_=0, to=100)
receipt_label.grid(row=2, column=1)
receipt_spinbox.grid(row=3, column=1)

for widget in info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Buttons
buttons_frame =LabelFrame(frame, text="Command Buttons")
buttons_frame.grid(row= 5, column=0, padx=20, pady=10)

add_button = Button(buttons_frame, text="Enter info", command= enter_data)
add_button.grid(row=0, column=1, padx=20, pady=10)

clear_button = Button(buttons_frame, text="Clear Info", command= clear)
clear_button.grid(row=0, column=2,  padx=10, pady=10)

delete_button = Button(buttons_frame, text="Delete Info", command= delete_data )
delete_button.grid(row=0, column=3,  padx=10, pady=10)

update_button = Button(buttons_frame, text="Update Info", command= update_data )
update_button.grid(row=0, column=4,  padx=10, pady=10)

#Table
table_frame =LabelFrame(frame, text="Data Table")
table_frame.grid(row= 7, column=0, padx=20, pady=10)


my_tree = ttk.Treeview(table_frame)

# Define columns
my_tree["columns"] = ("Name", "Item", "Quantity", "Receipt")


# Formate Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Name", width=120, stretch=NO)
my_tree.column("Item", anchor=CENTER, width=120)
my_tree.column("Quantity", width=100, anchor=CENTER)
my_tree.column("Receipt", width=140, anchor=CENTER)

# Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Item", text="Item", anchor=CENTER)
my_tree.heading("Quantity", text="Quantity", anchor=CENTER)
my_tree.heading("Receipt", text="Receipt", anchor=CENTER)


conn = sqlite3.connect('data.db')
cursor = conn.cursor()
rows = cursor.fetchall()
for row in rows:
    my_tree.insert(parent='', index='end', text="", values=(name_entry.get(),item_entry.get(),quantity_spinbox.get(),receipt_spinbox.get()))





my_tree.pack()





root.mainloop()