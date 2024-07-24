import tkinter as tk
import ttkbootstrap as ttk
import math
import random

FONT_NAME = "Courier"

class new():
    def __init__(self,root):
        self.buttoninteraction = {}

        self.Screen = ttk.Frame(root,width="800",height="500")
        self.Screen.pack(fill="both",expand=True)

        self.currentdis_withaccountname = None
        self.currentdis_Amount = None
        self.currentwith_Amount = None

        # create top frame +++
        topframe = ttk.Frame(self.Screen)
        topframe.pack(padx= 10,pady=5, fill="both")

        # bank name
        bankname = ttk.Label(topframe,text="Tech Fargo",font=(FONT_NAME,25))
        bankname.pack(anchor="w",side="left",expand=True)

        #f = ttk.Frame(topframe)
        #f.pack(side="bottom",expand=True)
        #self.welcometxt = ttk.Label(f,text="Welcome Billy421",font=(FONT_NAME,15))
        #self.welcometxt.pack(side="left")

        # create sign out button
        self.signout_btn = ttk.Button(topframe,text="Signout")
        self.signout_btn.pack(anchor="e",side="right")

        # create selection frame +++
        selectionFrame = ttk.Frame(self.Screen)
        selectionFrame.pack(fill="x")

        # Home Button
        self.homebutton = ttk.Button(selectionFrame,text="Home",command=lambda: self.buttonClicked("Home",None))
        self.homebutton.pack(side="left",expand=True,anchor="center",fill="x")

        self.sendMoneyButton = ttk.Button(selectionFrame,text="Pay",command=lambda: self.buttonClicked("Pay",None))
        self.sendMoneyButton.pack(side="left",expand=True,anchor="center",fill="x")

        
        # create main window +++
        mainwindow = ttk.Frame(self.Screen)
        mainwindow.pack(expand=True,fill="both")

        s = ttk.Style()
        s.configure("abc.TButton",background="blue" )
        s.configure("List.TButton",background="lightgray")

        s.configure("t.TLabel",background="")

        # Home Frame
        self.HomeFrame = ttk.Frame(mainwindow)
        self.HomeFrame.pack(expand=True,fill="both")

        self.accountFrame = ttk.Frame(self.HomeFrame)
        self.accountFrame.pack(expand=True)

        # deposit Frame
        self.DepositFrame = ttk.Frame(mainwindow)
        self.DepositFrame.pack(expand=True,fill="both")

        
        # withdrawl Frame
        self.WithdrawlFrame = ttk.Frame(mainwindow)
        self.WithdrawlFrame.pack(expand=True,fill="both")
        
        depinfo2 = ttk.Label(self.WithdrawlFrame,text="Input how much you want to Withdrawl.",font=(FONT_NAME,13))
        depinfo2.pack(pady=10)

        self.withInfoVar = tk.StringVar()
        box2 = ttk.Entry(self.WithdrawlFrame,textvariable=self.withInfoVar)
        box2.pack()

        ff2 = ttk.Frame(self.WithdrawlFrame)
        ff2.pack()

        self.cancelWithdrawlButton = ttk.Button(ff2,text="Cancel")
        self.cancelWithdrawlButton.pack(pady=10, padx=10,anchor="n")

        self.WithdrawlButton = ttk.Button(ff2,text="Withdrawl")
        self.WithdrawlButton.pack(pady=10,padx=1,anchor="n")

        depinfo = ttk.Label(self.DepositFrame,text="Input how much you want to deposit.",font=(FONT_NAME,13))
        depinfo.pack(pady=10)

        self.depInfoVar = tk.StringVar()
        box1 = ttk.Entry(self.DepositFrame,textvariable=self.depInfoVar)
        box1.pack()

        ff = ttk.Frame(self.DepositFrame)
        ff.pack()

        self.cancelDepositButton = ttk.Button(ff,text="Cancel")
        self.cancelDepositButton.pack(pady=10, padx=10,anchor="n")

        self.depositButton = ttk.Button(ff,text="Deposit")
        self.depositButton.pack(pady=10,padx=1,anchor="n")

        self.creditscoreFrame = ttk.Frame(self.HomeFrame)
        self.creditscoreFrame.pack(expand=True,fill="both")

        creditTitle = ttk.Label(self.creditscoreFrame,text="Credit",font=(FONT_NAME,20))
        creditTitle.pack()

        #Withdraw frame
        

        # credit selection frames for showing current credit
        self.creditselection = ttk.Frame(self.creditscoreFrame)
        self.creditselection.pack(expand=True,fill="both")

        self.creditList = ttk.Frame(self.creditselection)
        self.creditList.pack(side="left",expand=True)

        self.creditscoreButton = ttk.Frame(self.creditselection)
        self.creditscoreButton.pack(side="left",expand=True)
      
        # load accounts
        self.createAccountUI({"Name":"Checkings","Amount":random.randint(0,1000),"AccountNumber":294243290,"Account_Type":"Debit"})
       # self.createCreditAccountDescUI({"Name":"Checkings","Score":320,"AccountNumber":294243290})
        
        # credit score logic
        self.csUI = ttk.Frame(self.creditscoreButton,style="List.TButton", width=300,height=300)

        self.csFrame = ttk.Frame(self.creditscoreButton)

        self.acsTitle = ttk.Button(self.csUI,text="+Add Credit Score",command=self.openCreditScoreOption)
        self.acsTitle.pack()

        self.csinfo = ttk.Label(self.csFrame,text="What is your credit score?")
        self.csinfo.pack(fill="x")

        strVar = tk.StringVar()
        textbox = ttk.Entry(self.csFrame,textvariable=strVar)
        textbox.pack()

        self.sbox = ttk.Frame(self.csFrame)
        self.sbox.pack()

        confirm = ttk.Button(self.sbox,text="Confirm",command=lambda: creatCreditScore())
        confirm.pack(padx=5,pady=5, side="right")

        goback = ttk.Button(self.sbox,text="Go Back",command=self.closeCreditScoreOption)
        goback.pack(padx=5,pady=5,side="right")

        def creatCreditScore():
            print("go")
            v = strVar.get()
            try:
                v = int(v)
                self.createCreditAccountDescUI({"Name":"Credit","AccountNumber":453534534,"Score":v})
            except:
                 print("Error!")
            
        self.csUI.pack(expand=True)
        self.creditList.forget()

        # Transaction Frame
        self.TransactionFrame = ttk.Frame(mainwindow)
        self.TransactionFrame.pack(expand=True,fill="both")

        # Pay Frame
        self.PayFrame = ttk.Frame(mainwindow)
        self.PayFrame.pack(expand=True,fill="both")

        self.info1 = ttk.Label(self.PayFrame,text="Input the user name of who you want to pay.",font=(FONT_NAME,13))
        self.info1.pack()

        self.usernameVariable = tk.StringVar()
        box1 = ttk.Entry(self.PayFrame,textvariable=self.usernameVariable)
        box1.pack()

        self.info2 = ttk.Label(self.PayFrame,text="Please pick a account.",font=(FONT_NAME,13))
        self.info2.pack()

        self.pafsb = ttk.Frame(self.PayFrame)
        self.pafsb.pack(fill="x")

        self.selectedItem = ttk.Label(self.PayFrame, text="Selected: None")
        self.selectedItem.pack(pady=5)

        self.info3 = ttk.Label(self.PayFrame,text="How much you want to pay?")
        self.info3.pack(pady=2)

        self.payvariable = tk.StringVar()
        self.howmuch = ttk.Entry(self.PayFrame,textvariable=strVar)
        self.howmuch.pack(pady=2)

        self.paybutton = ttk.Button(self.PayFrame,text="Pay")
        self.paybutton.pack(pady=2)

        self.createAccountForPaymentUI({"Name":"Credit","AccountNumber":453534534,"Account_Type":"Debit","Amount":87670})

        self.windows = {
            "Home":self.HomeFrame,
            "Pay":self.PayFrame,
            "Withdrawl":self.WithdrawlFrame,
            "Deposit": self.DepositFrame,
        }

        self.buttonClicked("Home",None)
    
    def createAccountForPaymentUI(self,info):
        def selected():
             self.selectedItem.config(text="Selected: " + info.get("Name"))

        self.accUi = ttk.Frame(self.pafsb, style="List.TButton",width=300,height=300)
        title = ttk.Label(self.accUi,text=info.get("Name") + " (" + info.get("Account_Type") + ")",font=(FONT_NAME,15))
        title.pack(padx=5, anchor="w")

        balance = ttk.Label(self.accUi,text= "$" + str(random.randint(0,100)))
        balance.pack(anchor="w",pady=3,padx=35)

        alv_balance = ttk.Label(self.accUi,text= "Avaliable balance",font=(FONT_NAME,9))
        alv_balance.pack(padx=30,anchor="w")

        accNum = ttk.Label(self.accUi,text= "Account Number:" + str(info.get("AccountNumber")),font=(FONT_NAME,11))
        accNum.pack(padx=5,side="top")

        butt = ttk.Button(self.accUi,text="SelFect",command=selected)
        butt.pack(fill="x")

        self.accUi.pack(expand=True)


    def createAccountUI(self,info):
        self.Ui = ttk.Frame(self.accountFrame, style="List.TButton",width=300,height=300)
        title = ttk.Label(self.Ui,text=info.get("Name") + " (" + info.get("Account_Type") + ")",font=(FONT_NAME,15))
        title.pack(padx=5, anchor="w")

        self.accbals = {}
        self.accbals["a"+info.get("Name")] = tk.StringVar()

        asc = ttk.Label(self.Ui,text= "$" + str("{:.2f}".format(info.get("Amount"))),font=(FONT_NAME,15),textvariable=self.accbals["a"+info.get("Name")])
        asc.pack(anchor="w",pady=3,padx=35)

        self.accbals["a"+info.get("Name")].set("$" + str("{:.2f}".format(info.get("Amount"))))

        alv_balance = ttk.Label(self.Ui,text= "Avaliable balance",font=(FONT_NAME,9))
        alv_balance.pack(padx=30,anchor="w")

        accNum = ttk.Label(self.Ui,text= "Account Number:" + str(info.get("AccountNumber")),font=(FONT_NAME,11))
        accNum.pack(padx=5,side="top")

        self.abc = ttk.Frame(self.Ui)
        self.abc.pack(fill="x")

        self.buttoninteraction[info.get("Name") + "Deposit"] = ttk.Button(self.abc,text="Deposit",command=lambda: self.buttonClicked("Deposit",info.get("Name")))
        self.buttoninteraction[info.get("Name") + "Deposit"].pack(pady=5,expand=True,fill="both",side="left")

        self.buttoninteraction[info.get("Name") + "Withdraw"] = ttk.Button(self.abc,text="Withdraw",command=lambda: self.buttonClicked("Withdrawl",info.get("Name")))
        self.buttoninteraction[info.get("Name") + "Withdraw"].pack(pady=5,expand=True,fill="both",side="left")

        self.Ui.pack(expand=True)

    def createCreditAccountDescUI(self,info):
        self.Ui = ttk.Frame(self.creditList,style="List.TButton", width=300,height=300)
        title = ttk.Label(self.Ui,text=info.get("Name") + "(.... " + str(info.get("AccountNumber"))[-4:],font=(FONT_NAME,15))
        title.pack(padx=5, anchor="w")

        score = ttk.Label(self.Ui,text= info.get("Score"),font=(FONT_NAME,15))
        score.pack(anchor="center",pady=3)

        t = None
        if info["Score"] <= 540:
             t = "Your Credit Score Is Really Bad"
        elif info["Score"] <= 630 and info["Score"] > 689:
            t = "Your Credit Score Is Fair"
        elif info["Score"] <=690 and info["Score"] > 719:
             t = "Your Score Is Good"
        elif info["Score"] <= 720 and info["Score"] > 850:
             t = "Your Score Is Excelent!"

        status = ttk.Label(self.Ui,text= t,font=(FONT_NAME,9))
        status.pack()
        self.creditList.pack()
        self.Ui.pack(expand=True)
        self.creditscoreButton.forget()

    def openCreditScoreOption(self):
            self.csUI.forget()
            self.csFrame.pack(expand=True)
            self.acsTitle.forget()

    def closeCreditScoreOption(self):
            self.csUI.pack(expand=True)
            self.csFrame.forget()
            self.acsTitle.pack()

    
    def buttonClicked(self,name_,getvalue):
        self.currentdis_withaccountname = getvalue
        self.closeCreditScoreOption()
        for name in self.windows:
            if name_ == name:
                self.windows[name].pack(pady=10,expand=True,fill="both")
            else:
                self.windows[name].forget()
        

        