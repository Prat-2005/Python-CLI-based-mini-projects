# 2. Simple Banking System (Console App)

class InsufficientFundsError(Exception):
    def __init__(self, amt, msg = "Your balance is insufficient to withdraw"):
        self.amt = amt
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"Transaction failed! {self.msg}.\n"
    
def transaction_history(stmt):
    with open("transactions.txt", "a") as file:
        file.write(stmt)


bal = 12000
ch = ""

while ch != '5':
    print("Connnected to service! What do you like to choose?")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check balance")
    print("4. Transaction History")
    print("5. Exit")

    ch = input("Enter your choice:")

    try:
        if ch == '1':
            print("You are depositing the money...")
            amt = int(input("Enter the amount you want to deposit:"))
            if amt <= 0:
               print("Amount must be greater than zero.\n")
               continue
            bal += amt
            stmt = f"Rs.{amt} credited into your account.\n"
            print(stmt)
            transaction_history(stmt)
        elif ch == '2':
            print("You are withdrawing the money...")
            amt = int(input("Enter the amount you want to wthdraw:"))
            if amt <= 0:
               print("Amount must be greater than zero.\n")
               continue
            if amt > bal:
                raise InsufficientFundsError(amt)
            bal -= amt
            stmt = f"Rs.{amt} debited from your account.\n"
            print(stmt)
            transaction_history(stmt)
        elif ch == '3':
            print(f"Your bank balance: {bal}\n")
        elif ch == '4':
            with open("transactions.txt", "r") as file:
                history = file.read()
                print(history)
        elif ch == '5':
            print("Disconnected from service.....")
        else:
            print("Invalid input! Please enter choice number (1-4).\n")
    except ValueError as e:
        print("ERROR! Amount must be in numbers not in words.\n")
    except InsufficientFundsError as e:
        print(e)
        