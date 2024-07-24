import Account_Manager
import HomePage

userdata = {"personal": # example
                      {"Name":"Doe","Email":"John.doe@gmail.com","Ethnicity":"White","Birthdate":"1/1/1000","Phone_Number":"1234567890"},
                      "DefaultAccount":
                      {"Amount":25,"Frozen":False,"Account_Type":"Debit"}}

na = Account_Manager.Create_User(userdata)
