import tkinter as tk
from tkinter import messagebox
class ContactMaster:
    def __init__(self):
        self.contacts = {}

    # Add a new contact
    def add_contact_num(self,name,phone_number):
        if name in self.contacts:
            return f"Contact '{name}' exists already."
        else:
            self.contacts[name] = phone_number
            return f"Contact '{name}' added successfully."

    # Delete an existing contact
    def delete_contact_num(self,name):
        if name in self.contacts:
            del self.contacts[name]
            return f"Contact '{name}' deleted successfully."
        else:
            return f"Contact '{name}' not found."

    # Search for a contact by name
    def search_contact_num(self,name):
        if name in self.contacts:
            return f"{name}: {self.contacts[name]}"
        else:
            return f"Contact '{name}' not found."

    # Display all contacts
    def display_contacts(self):
        if self.contacts:
            return "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        else:
            return "No contacts available."

class CMGUI:
    def __init__(self, root):
        self.gui = ContactMaster()
        self.root = root
        self.root.title("ContactMaster")

        # UI Elements
        self.name_label = tk.Label(root,text="Name:")
        self.name_label.grid(row=0,column=0,padx=10,pady=5)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0,column=1,padx=10,pady=5)

        self.phone_label = tk.Label(root,text="Phone:")
        self.phone_label.grid(row=1,column=0,padx=10,pady=5)

        self.phone_num_entry = tk.Entry(root)
        self.phone_num_entry.grid(row=1,column=1,padx=10,pady=5)

        self.add_button = tk.Button(root,text="Add Contact", command=self.add_contact_num)
        self.add_button.grid(row=2, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(root,text="Delete Contact", command=self.delete_contact_num)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

        self.search_button = tk.Button(root, text="Search Contact",command=self.search_contact_num)
        self.search_button.grid(row=3,column=0, padx=10,pady=5)

        self.display_button = tk.Button(root,text="Display All Contacts", command=self.display_contact_nums)
        self.display_button.grid(row=3,column=1, padx=10, pady=5)

        self.output_text = tk.Text(root,height=10,width=50, state='disabled')
        self.output_text.grid(row=4,column=0,columnspan=2, padx=10, pady=5)

    def add_contact_num(self):
        name = self.name_entry.get()
        phone = self.phone_num_entry.get()
        if name and phone:
            message = self.gui.add_contact_num(name, phone)
        else:
            message = "Please enter name and phone number."
        self.show_message(message)

    def delete_contact_num(self):
        name = self.name_entry.get()
        if name:
            message = self.gui.delete_contact_num(name)
        else:
            message = "Please enter the name to delete."
        self.show_message(message)

    def search_contact_num(self):
        name = self.name_entry.get()
        if name:
            message = self.gui.search_contact_num(name)
        else:
            message = "Please enter the name to search."
        self.show_message(message)

    def display_contact_nums(self):
        message = self.gui.display_contacts()
        self.output_text.configure(state='normal')
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.configure(state='disabled')

    def show_message(self, message):
        messagebox.showinfo("ContactMaster", message)


root = tk.Tk()
gui = CMGUI(root)
root.mainloop()
