credit_score = int(input("Enter your credit score:"))
if credit_score > 690 or (credit_score > 800 and credit_score < 850):
    print("You have a great credit score")
elif credit_score < 690 and credit_score > 0:
    print("You need to improve your credit score")
else:
    print("Invalid entry")