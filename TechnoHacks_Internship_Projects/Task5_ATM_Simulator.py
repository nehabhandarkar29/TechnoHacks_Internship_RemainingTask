class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        """Function to check account balance"""
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        """Function to deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
            self.check_balance()
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self, amount):
        """Function to withdraw money from the account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.check_balance()
        else:
            print("Insufficient funds or invalid amount. Withdrawal failed.")

def main():
    atm = ATM()
    
    while True:
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
