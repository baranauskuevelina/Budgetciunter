import pickle

def load_budget():
    try:
        with open('budget.pickle', 'rb') as file:
            budget = pickle.load(file)
    except FileNotFoundError:
        budget = {'balance': 0, 'revenue': 0}
    return budget

def save_budget(budget):
    with open('budget.pickle', 'wb') as file:
        pickle.dump(budget, file)

def main():
    budget = load_budget()

    while True:
        print(f"Balance: ${budget['balance']}")
        print(f"Revenue: ${budget['revenue']}")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Income amount: "))
                budget['balance'] += amount
                budget['revenue'] += amount
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '2':
            try:
                amount = float(input("Expense amount: "))
                if amount > budget['balance']:
                    print("Insufficient balance.")
                else:
                    budget['balance'] -= amount
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            print("Exiting...")
            save_budget(budget)
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
