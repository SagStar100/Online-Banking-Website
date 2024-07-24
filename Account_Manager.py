import tkinter as tk
import ttkbootstrap as ttk
import UserData

UserData.load()

def isAccountNameUnique(User:dict, name): # Check if any existing accounts the user have has the same name as the new account
    for accName in User.UserInfo["Accounts"]:
        if accName == name:
           return False
    return True

def doesAccountExist(User:dict, name):
    try:
        return name in User.UserInfo["Accounts"]
    except:
        print("Accout Error" , User)
        return True

def doesAccountHaveEnoughFunds(User:dict,AccountName:str,Amount:float):
    if not doesAccountExist(User,AccountName): # If account doesnt exist
        return
    
    try:
        return User.UserInfo["Accounts"][AccountName]["Amount"] >= Amount
    except:
        try:
            return User["Accounts"][AccountName]["Amount"] >= Amount
        except:
            print(User)
    

def getNumOfUserAccounts(User): # Gets the number of user accounts
    n = 0
    for i in User.UserInfo["Accounts"]:
        n += 1
    return n

def createAccountType(User: dict,Information: dict): # create a new account for the user
    if doesAccountExist(User,Information.get("Name")):
        # error user
        return

    User.UserInfo["Accounts"][Information.get("Name")] = {
        "Amount": Information.get("Amount",0),
        "Frozen": Information.get("Frozen",False), # If account is frozen then do not make any transactions
        "Account_Type": Information.get("Account_Type","N/A"), # There must be a valid account type (credit or debit)
        "AccountNumber": 0, # we will configure this later
    }

    UserData.updateData(User)

def removeAccountType(User:dict,AccountName:str):
    if getNumOfUserAccounts(User) - 1 <= 0:
        return # we can not have no accounts in this users account

    if not doesAccountExist(User,AccountName):
        return
    
    amount = User.UserInfo["Accounts"][AccountName]["Amount"]
    del User.UserInfo["Accounts"][AccountName]

    # check if the default account is the account we just deleted
    if User.UserInfo["Settings"]["Default_Account"] == AccountName:
        nextAccount = None
        for i in User.UserInfo["Accounts"]:
            nextAccount = i
        # make new default account
        setDefaultAccountType(User,nextAccount)


    #We will put the remaining balance from the deleted account to the default_account
    User.UserInfo["Accounts"][User.UserInfo["Settings"]["Default_Account"]]["Amount"] += amount

    UserData.updateData(User)

def setDefaultAccountType(User,AccountName):
    if not doesAccountExist(User,AccountName):
        return
    
    # set new default account method for money sending
    User.UserInfo["Settings"]["Default_Account"] = AccountName

def freezeAccount(User,AccountName):
    if not doesAccountExist(User,AccountName):
        return
    
    User.UserInfo["Accounts"][AccountName]["Frozen"] = True

def freeze_All_Accounts(User):
    User.UserInfo["Settings"]["All_Acc_Frozen"] = True

def deposit(User,AccountName,Amount):
    if not doesAccountExist(User,AccountName):
        # warn user
        return
    
    # check if the amount in the giving account has enough funds
    if not doesAccountHaveEnoughFunds(User,AccountName,Amount):
        return

    User.UserInfo["Accounts"][AccountName]["Amount"] -= Amount

def Withdrawl(User,AccountName,Amount):
    if not doesAccountExist(User,AccountName):
        # warn user
        return
    
    # check if the amount in the giving account has enough funds
    if not doesAccountHaveEnoughFunds(User,AccountName,Amount):
        return

    User.UserInfo["Accounts"][AccountName]["Amount"] += Amount

def Transfer_Money_To_Account(User:dict,Account_Giving:str,Account_Recieving:str,Amount:float):
    # check if both accounts exist
    if not doesAccountExist(User,Account_Giving) or not doesAccountExist(User,Account_Recieving):
        # warn user
        return
    
    # check if the amount in the giving account has enough funds
    if not doesAccountHaveEnoughFunds(User,Account_Giving,Amount):
        return
    
    # Transfer Account logic
    User["Accounts"][Account_Giving]["Amount"] -= Amount
    User["Accounts"][Account_Recieving]["Amount"] += Amount

def Send_Money_To_User(User_Giving,User_Recieving,AccountName:str,Amount:float): # TEST
    # check if the player has the checkings
    if not doesAccountExist(User_Giving,AccountName) or not doesAccountExist(User_Recieving,User_Giving.UserInfo["Settings"]["Default_Account"]):
        # warn user if their account doesnt exist, or the other users default account exist
        return
    
    # check if the account is frozen on all accounts
    if User_Giving.UserInfo["Settings"]["All_Acc_Frozen"]:
        return # accounts are frozen
    
    # check if the account is frozen on the specific account
    if User_Giving.UserInfo["Accounts"][AccountName]["Frozen"]:
        return

    # if the reciever account is frozen on all accounts
    if User_Recieving.UserInfo["Settings"]["All_Acc_Frozen"]:
        return

    # if specific account is frozen on the reciever
    if User_Recieving.UserInfo["Accounts"][User_Recieving.UserInfo["Settings"]["Default_Account"]]["Frozen"]:
        return
    
    # check if the amount in the giving account has enough funds
    if not doesAccountHaveEnoughFunds(User_Giving,AccountName,Amount):
        return
    
    # begin sending money
    User_Giving.UserInfo["Accounts"][AccountName]["Amount"] -= Amount
    User_Recieving.UserInfo["Accounts"][User_Recieving.UserInfo["Settings"]["Default_Account"]]["Amount"] += Amount
        
class Create_User():
    def __init__(self,Information: dict):
        if not UserData.isUserNameUnique(Information["personal"].get("UserName")):
            print("UserName Is not Unique!")
            return
        # set information in a table
        self.UserInfo = { # (use data frame to store information)
            "Personal_Information": {
                "UserName": Information["personal"].get("UserName","N/A"),
                "Name":Information["personal"].get("Name","N/A"), # First_Middle_Last
                "Email":Information["personal"].get("Email","N/A"),
                "Ethnicity":Information["personal"].get("Ethnicity","N/A"),
                "Birthdate":Information["personal"].get("Birthdate","N/A"),
                "Phone_Number":Information["personal"].get("Phone_Number","N/A"),
                "Password":Information["personal"].get("Password","N/A"),
                "Id":0, # this will be altered later
            },
            "Accounts":{},
            "Settings":{"All_Acc_Frozen":False,"Default_Account":None}
        }

        # create default deposit account
        createAccountType(self,{
            "Name": "Checkings",
            "Amount": float(25),
            "Frozen": False,
            "Account_Type": "Debit"
        })

        # Set default account type
        setDefaultAccountType(self,"Checkings")

        # create data
        UserData.updateData(self)

newAcc = Create_User({"personal": # example
                      {"UserName":"Billy420", "Name":"John","Email":"John.doe@gmail.com","Ethnicity":"White","Birthdate":"1/1/1000","Phone_Number":"1234567890","Password":"idk347"},
                      "DefaultAccount": 
                      {"Amount":float(25),"Frozen":False,"Account_Type":"Debit"}
                      })

newAcc2 = Create_User({"personal": # example
                      {"UserName":"Willian","Name":"William","Email":"John.doe@gmail.com","Ethnicity":"White","Birthdate":"1/1/1000","Phone_Number":"1234567890","Password":"CheeseCake805"},
                      "DefaultAccount": 
                      {"Amount":float(25),"Frozen":False,"Account_Type":"Debit"}
                      })

newAcc3 = Create_User({"personal": # example
                      {"UserName":"Blaire","Name":"William","Email":"John.doe@gmail.com","Ethnicity":"White","Birthdate":"1/1/1000","Phone_Number":"1234567890","Password":"Blaire"},
                      "DefaultAccount": 
                      {"Amount":float(25),"Frozen":False,"Account_Type":"Debit"}
                      })

newAcc4 = Create_User({"personal": # example
                      {"UserName":"Boby","Name":"William","Email":"John.doe@gmail.com","Ethnicity":"White","Birthdate":"1/1/1000","Phone_Number":"1234567890","Password":"Brown"},
                      "DefaultAccount": 
                      {"Amount":float(25),"Frozen":False,"Account_Type":"Debit"}
                      })

createAccountType(newAcc,{
            "Name": "Savings_2.0",
            "Amount": float(7),
            "Frozen": False,
            "Account_Type": "Debit"
        })


print(UserData.getdata("Billy421"))
