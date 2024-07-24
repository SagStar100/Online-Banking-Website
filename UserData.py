import os
import csv

Data_Key = "key.csv"
Directory = os.getcwd() + "/" + Data_Key
MAX_ACCOUNT_CREATIONS = 3

placeholder = ["Id","UserName","Name","Birthdate","Ethnicity","Phone_Number","Password","Email","All_Acc_Frozen","Default_Account"]
accountPlaceholder = ["Amount","AccountNumber","Frozen","Account_Type"]

for i in range(MAX_ACCOUNT_CREATIONS):
    placeholder.append("Account_Name_" + str(i + 1))
    placeholder.append("Account_Amount_" + str(i + 1))
    placeholder.append("Account_AccountNumber_" + str(i+1))
    placeholder.append("Account_Frozen_" + str(i + 1))
    placeholder.append("Account_Account_Type_" + str(i + 1))

def load():
    if not os.path.exists(Directory):
        # create csv file
        with open(Directory,'w',newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(placeholder)
            print("Created Student Data CSV")
    else:
        pass

load()

def User_LogIn_Attempt(UserName:str,Password:str):
    with open(Directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == UserName and row[6] == Password:
                    return True
    return False
                
    

def updateData(User:dict):
    if not getdata(User.UserInfo["Personal_Information"]["UserName"]):
        ui = User.UserInfo
        pi = ui["Personal_Information"]
        a = ui["Accounts"]
        s = ui["Settings"]

        data = []

        # get data from the personal inforation and the settings
        for i in range(len(placeholder)):
            if pi.get(placeholder[i]) != None:
                data.append(pi.get(placeholder[i]))

            if s.get(placeholder[i]) != None:
                data.append(s.get(placeholder[i]))

        for name in a:
            data.append(name)
            data.append(a[name]["Amount"])
            data.append(a[name]["AccountNumber"])
            data.append(a[name]["Frozen"])
            data.append(a[name]["Account_Type"])
        
        # Write the data to the CSV file (Save data)
        with open(Directory, 'a', newline='') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)
            # add data to CSV
            csv_writer.writerow(data)
    else:
        print("Get Current Data and fuck with it")

def isUserNameUnique(UserName:dict):
    with open(Directory,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == UserName:
                return False
    return True




def getdata(UserName:str):
    data = None
    with open(Directory,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[1] , UserName)
                if row[1] == UserName:
                    data = {
                        "Personal_Information": {},
                        "Accounts":{},
                        "Settings":{}
                    }
                        
                    for i in range(1,9):
                        if i <=7:
                            data["Personal_Information"][placeholder[i]] = row[i]
                        elif i>=8 and i<=9:
                            data["Settings"][placeholder[i]] = row[i]

                    #for i in range(9 + 1):
                        #data["Personal_Information"][placeholder[i]]: row[i]
                    for i in range(1,len(row)):
                        if (10 + (i-1))%5 == 0:
                            try:
                                data["Accounts"][row[10 + (i-1)]] = {}
                                for u in range(10 + (i-1) + 1,(10 + (i-1)) + 5):
                                    num = int(str(u)[1]) - 1

                                    data["Accounts"][row[10 + (i-1)]][accountPlaceholder[num]] = row[u]
                            except:
                                pass
                        
    return data

getdata("Billy420")
