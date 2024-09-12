
class InsufficientBalanceException(Exception):
    """Custom exception for insufficient balance during withdrawal."""
    pass

class Account:
    def __init__(self, account_number, name, initial_deposit):
        self.account_number = account_number
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            raise InsufficientBalanceException(f"Cannot withdraw {amount}. Minimum balance of 1000 must be maintained.")
        self.balance -= amount
        print(f"Amount withdrawn: {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = input("Enter account number: ")
        name = input("Enter account holder's name: ")
        initial_deposit = float(input("Enter initial deposit: "))
        if initial_deposit < 1000:
            print("Initial deposit must be at least 1000.")
            return
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        print(f"Account created successfully for {name} with account number {account_number}.")

    def deposit_amount(self):
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            print("Account not found.")
            return
        amount = float(input("Enter amount to deposit: "))
        self.accounts[account_number].deposit(amount)

    def withdraw_amount(self):
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            print("Account not found.")
            return
        amount = float(input("Enter amount to withdraw: "))
        try:
            self.accounts[account_number].withdraw(amount)
        except InsufficientBalanceException as e:
            print(e)

    def check_balance(self):
        account_number = input("Enter account number: ")
        if account_number not in self.accounts:
            print("Account not found.")
            return
        self.accounts[account_number].check_balance()

    def show_menu(self):
        while True:
            print("\n*** Bank Menu ***")
            print("1. Welcome Message")
            print("2. Create Account")
            print("3. Deposit Amount")
            print("4. Withdraw Amount")
            print("5. Check Account Balance")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                print("Welcome to the Bank! How can we assist you today?")
            elif choice == '2':
                self.create_account()
            elif choice == '3':
                self.deposit_amount()
            elif choice == '4':
                self.withdraw_amount()
            elif choice == '5':
                self.check_balance()
            elif choice == '6':
                print("Thank you for banking with us. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the Bank Application
if __name__ == "__main__":
    bank = Bank()
    bank.show_menu()
