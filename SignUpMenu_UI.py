
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

#import info

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
                
# Allow the user to create their own username
def create_username(event,userNameVar):
    
    username = userNameVar.get()

    # Check if username is certain length and contains certain characters
    if len(username) >= 10:
        if username[0].isupper() == True:
            if " " not in username:
                print("First charcter is uppercase, is long, has no spaces")
                return True
            else:
                messagebox.showinfo(title="Invalid Username", message="Username must be 10 characters long, first letter must be upper case, have no spaces")
                return False
        else:
            messagebox.showinfo(title="Invalid Username", message="Username must be 10 characters long, first letter must be upper case, have no spaces")
            return False
    else:
        messagebox.showinfo(title="Invalid Username", message="Username must be 10 characters long, first letter must be upper case, have no spaces")
        return False



# Allow the user to create their own password
def create_password(event,passwordVar):
    password = passwordVar.get()

    special_chars = [
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']',
    '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '¥', '€', '£'
]
    letter_count = sum(1 for char in password if char.isalpha())

    if len(password) >= 12:
        if password[0].isupper() == True:
            if " " not in password:
                if any(char.isdigit() for char in password):
                    if (letter_count >= 10):
                        if any(char in special_chars for char in password):
                            print("All conditions met")
                            return True
                        else:
                            messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
                            return False
                    else:
                        messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
                        return False
                else:
                    messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
                    return False
            else:
                messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
                return False
        else:
            messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
            return False
    else:
        messagebox.showinfo(title="Invalid Password", message="Password must be 12 characters long, first letter must be upper case, have no spaces, contain 1 number, contain 1 special character")
        return False
    
    #info.display()

class new():
    def __init__(self,root):
        self.Screen = ttk.Frame(root,width="800",height="500")
        self.Screen.pack(fill="both",expand=True)

    # Creatas the Labels
        self.menu_title = ttk.Label(self.Screen,text= "Sign Up and Start Banking", font = (FONT_NAME, 15))
        self.username_website = ttk.Label(self.Screen,text="Username:")
        self.password_website = ttk.Label(self.Screen,text="Password:")

        # Entry
        self.userNameVar = tk.StringVar()
        self.passwordVar = tk.StringVar()

        self.entry_username = ttk.Entry(self.Screen,width = 21,textvariable=self.userNameVar)
        self.entry_username.bind("<Return>", lambda event: create_username(self.userNameVar))

        self.entry_password = ttk.Entry(self.Screen,width = 21, textvariable=self.passwordVar)
        self.entry_password.bind("<Return>", lambda event: create_password(self.passwordVar))
        self.entry_password.config(show="*")

        # Buttons
        self.buttonframe = ttk.Frame(self.Screen)
        self.sign_in_btn = ttk.Button(self.buttonframe,text="Sign In", width=10)
        self.sign_up_btn = ttk.Button(self.buttonframe,text="Sign Up", width=10)

        self.menu_title.pack(expand=True)
        self.username_website.pack(expand=True)
        self.entry_username.pack(expand=True)
        self.password_website.pack(expand=True)
        self.entry_password.pack(expand=True)

        self.buttonframe.pack(expand=True)
        self.sign_in_btn.pack(padx = 5,expand=True,side="left")
        self.sign_up_btn.pack(expand=True,side="left")
