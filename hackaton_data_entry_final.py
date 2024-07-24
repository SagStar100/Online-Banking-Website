class PersonalInfo:
    def __init__(self):
        self.numbers = ""
        self.letters = ""
        self.ssn = ""
        self.name = ""


ID = PersonalInfo()


class Credit:
    def __init__(self):
        self.score = 0


credit_update = Credit()


class Deposit:
    def __init__(self):
        self.value = PersonalInfo()
        self.balance = 0.0


adding = Deposit()


class Type:
    def __init__(self):
        self.type_of_account = ""


account_type = Type()


def main():
    print("Enter the name to be on your account:")
    ID.name = input()
    print("Enter a password starting with numbers: ")
    ID.numbers = input()
    print("Enter a password with remaining letters: ")
    ID.letters = input()
    print("New pasword combined:\n", ID.numbers + ID.letters)
    print("Enter your SSN value: ")
    ID.ssn = input()
    print("Enter your credit score: ")
    credit_update.score = int(input())
    print("Please enter the account type:")
    account_type.type_of_account = input()
    if credit_update.score > 690 or (
        credit_update.score > 800 and credit_update.score < 850
    ):
        print("You are doing great with your credit score !!")
    else:
        print("Here are some tips to help improve your credit score:")
        print("A. Keep a budget and stop uneccesary spendings")
        print("B. cut down on exntertainment and other costly vacation trips")
        print("C. Ask for a free consultation to go")


if __name__ == "__main__":
    main()
    print("\nEnter a deposit balance of atleast $25\n")
adding.balance = float(input())
if adding.balance >= 25:
    print("Balance added-(new amount): $%.2f\n" % adding.balance)
else:
    print("Insuffiencent funds please add more to continue inital account set up")
values = ID.numbers
social = ID.ssn
credit_score = credit_update.score
Letter_value = ID.letters
name = ID.name
account_types = account_type.type_of_account
print("\n")
print("Summary of account creation:\n")
print("Name:%s" % name)
print("Newly created Password:%s%s" % (values, Letter_value))
print("SSN:%s" % social)
print("credit_score:%d" % credit_score)
print("balance:$%.2f" % adding.balance)
print("Account type:%s" % account_types)
