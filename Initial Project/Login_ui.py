import tkinter as tk
from tkinter import messagebox

def store_credentials(username, password):
    global stored_username, stored_password
    stored_username = username
    stored_password = password

def show_info(info_type):
    if info_type == "username":
        messagebox.showinfo("Username", f"Username: {stored_username}")
    elif info_type == "password":
        messagebox.showinfo("Password", f"Password: {stored_password}")

def open_user_interface():
    ui = tk.Tk()
    ui.title("User Interface")
    tk.Button(ui, text="View Username", command=lambda: show_info("username")).pack(padx=20, pady=10)
    tk.Button(ui, text="View Password", command=lambda: show_info("password")).pack(padx=20, pady=10)
    tk.Button(ui, text="Exit", command=ui.destroy).pack(padx=20, pady=10)
    ui.mainloop()

def login():
    username = entry_username.get()
    password = entry_password.get()
    store_credentials(username, password)
    messagebox.showinfo("Login", "Credentials stored!")
    root.destroy()  # Close the login window
    open_user_interface()

def create_login_ui():
    global root, entry_username, entry_password
    root = tk.Tk()
    root.title("Login UI")

    tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()

create_login_ui()