

def main():
    balance = 0
    is_running = True

    def show_balance():
        print(f"Your balance is ${balance:.2f}")

    def deposit():
        amount = float(input("Enter deposit amount: "))
        if amount < 0:
            print("invalid amount")
            return 0
        else:
            return amount

    def withdraw():
        amount = float(input("Enter withdraw amount: "))
        if amount < 0 or amount > balance:
            print("invalid amount")
            return 0
        else:
            return amount


    while is_running:
        print("---------- Banking Program ----------")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw()
        elif choice == "4":
            is_running = False
        else:
            print(f"{choice} is not a valid choice!")

    print("--------- Thank you! ----------")


if __name__ == "__main__":
    main()