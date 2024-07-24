
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

#import info

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
                
# Allow the user to create their own username
def create_username(event,userNameVar): 
    username = userNameVar.get()

# Allow the user to create their own password
def create_password(event,passwordVar):
    password = passwordVar.get()

class new():
    def __init__(self,root):
        self.Screen = ttk.Frame(root,width="800",height="500")
        self.Screen.pack(fill="both",expand=True)

    # Creatas the Labels
        self.menu_title = ttk.Label(self.Screen,text= "Sign in and Start Banking", font = (FONT_NAME, 15))
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
        self.sign_in_btn = ttk.Button(self.Screen,text="Sign In", width=10)

        self.menu_title.pack(expand=True)
        self.username_website.pack(expand=True)
        self.entry_username.pack(expand=True)
        self.password_website.pack(expand=True)
        self.entry_password.pack(expand=True)
        self.sign_in_btn.pack(expand=True)
