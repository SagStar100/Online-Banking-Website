import tkinter as tk
import ttkbootstrap as ttk

import UserData

import LoginMenu_UI
import HomePortal_UI
import SignUpMenu_UI

import Account_Manager

UserName = "Billy421"

Screen = ttk.Window(themename="darkly")
Screen.title("Tech Fargo Here")
Screen.resizable(False,False)
Screen.geometry("800x525")

container = ttk.Frame()
container.pack(expand=True,fill="both")

LoginMenu_Frame = LoginMenu_UI.new(container)
SignUpMenu_Frame = SignUpMenu_UI.new(container)
HomePortal_Frame = HomePortal_UI.new(container)

# connections
# Will check if create user name and password functions return true and give them a unique ID (map to sign up button)
def check_credentials(event,unVar,pwVar):
    if UserData.User_LogIn_Attempt(unVar,pwVar):
        UserName = unVar
    showHomePortal()
    #else:
        #print("error")

LoginMenu_Frame.sign_in_btn.bind("<Button-1>", lambda event: check_credentials(None,LoginMenu_Frame.userNameVar.get(),LoginMenu_Frame.passwordVar.get()))  # Binds lefdt click button to the Sign Up button
HomePortal_Frame.signout_btn.bind("<Button-1>", lambda event: showLoginMenu())

# cancel logic
HomePortal_Frame.cancelDepositButton.bind("<Button-1>", lambda event: HomePortal_Frame.buttonClicked("Home",None))
HomePortal_Frame.cancelWithdrawlButton.bind("<Button-1>", lambda event: HomePortal_Frame.buttonClicked("Home",None))


def deposit():
    data = UserData.getdata(UserName)
    Account_Manager.deposit(data,HomePortal_Frame.currentdis_withaccountname,HomePortal_Frame.depInfoVar)

    #HomePortal_Frame.accbals["a"+HomePortal_Frame.currentdis_withaccountname].set("$" + str("{:.2f}".format(data["UserInfo"]["Accounts"][HomePortal_Frame.currentdis_withaccountname]["Amount"])))

    HomePortal_Frame.buttonClicked("Home",None)

def withdrawl():
    Account_Manager.Withdrawl(UserData.getdata(UserName),HomePortal_Frame.currentdis_withaccountname,HomePortal_Frame.withInfoVar)
    HomePortal_Frame.buttonClicked("Home",None)

    

# deposit withdrawl logic
HomePortal_Frame.depositButton.bind("<Button-1>", lambda event: deposit())
HomePortal_Frame.WithdrawlButton.bind("<Button-1>", lambda event: withdrawl())

def showHomePortal():
    HomePortal_Frame.buttonClicked("Home",None)

    LoginMenu_Frame.Screen.forget()
    SignUpMenu_Frame.Screen.forget()
    HomePortal_Frame.Screen.pack(expand=True,fill="both")

def showLoginMenu():
    UserName = None
    HomePortal_Frame.buttonClicked("Home",None)

    LoginMenu_Frame.Screen.pack(expand=True,fill="both")
    SignUpMenu_Frame.Screen.forget()
    HomePortal_Frame.Screen.forget()

showLoginMenu()

Screen.mainloop()