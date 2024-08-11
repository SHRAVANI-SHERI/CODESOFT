import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Contact dictionary to store contacts
        self.contacts = {}

        # Create the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Frame for input fields
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Name label and entry
        tk.Label(self.frame, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Phone label and entry
        tk.Label(self.frame, text="Phone:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.frame, width=30)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add Contact Button
        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Listbox for displaying contacts
        self.contacts_listbox = tk.Listbox(self.root, width=50, height=10)
        self.contacts_listbox.pack(padx=10, pady=10)

        # Buttons for actions
        self.view_button = tk.Button(self.root, text="View Contact", command=self.view_contact)
        self.view_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        
        if name and phone:
            if name in self.contacts:
                messagebox.showwarning("Warning", "Contact already exists!")
            else:
                self.contacts[name] = phone
                self.contacts_listbox.insert(tk.END, name)
                self.name_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Both name and phone are required!")

    def view_contact(self):
        selected = self.contacts_listbox.curselection()
        if selected:
            name = self.contacts_listbox.get(selected[0])
            phone = self.contacts.get(name, "No phone number available")
            messagebox.showinfo("Contact Info", f"Name: {name}\nPhone: {phone}")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to view!")

    def delete_contact(self):
        selected = self.contacts_listbox.curselection()
        if selected:
            name = self.contacts_listbox.get(selected[0])
            del self.contacts[name]
            self.contacts_listbox.delete(selected[0])
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
