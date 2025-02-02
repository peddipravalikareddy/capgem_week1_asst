# ATM

# Initial balance of the user (for demonstration purposes)
balance = 1000

# Function to check the balance
def check_balance():
    balance
    print(f"Current balance is: {balance}")

# Function to deposit money
def deposit_money():
    balance
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            balance += amount
            print(f"${amount} has been deposited successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to withdraw money
def withdraw_money():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance for this withdrawal.")
        else:
            balance -= amount
            print(f"${amount} has been withdrawn successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main function to simulate ATM menu
def atm_menu():
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        try:
            choice = int(input("Please choose an option (1-4): "))
            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit_money()
            elif choice == 3:
                withdraw_money()
            elif choice == 4:
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the ATM simulation
atm_menu()
