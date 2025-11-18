

# initial Interaction 


def default_budget_allocation():
    print("General rule of thumb is to allocate your budget as follows: \n"
    "- 50% Needs (Rent, Utilities, Groceries)\n"
    "- 30% Wants (Dining Out, Entertainment)\n"
    "- 20% Savings (Emergency Fund, Investments)\n")

def budget_allocation(budget_amount):
    print("Your budget would look like this using general practice:")
    needs = budget_amount * .50
    wants = budget_amount * .30
    savings = budget_amount * .20
    print(f"Budget Amount: ${budget_amount}")
    print(f"Needs: ${needs}")
    print(f"Wants: ${wants}")
    print(f"Savings: ${savings}")

print("Budgeting App \n" \
"Manage your finances effectively!\n" \
"-----------------------------------\n" \
"") 


def budget_intro():
    print("How much do you want to budget with today?")
    user_input = input("Enter Here: $")

    try:
        amount = float(user_input)
        
    except ValueError:
            print("Invalid input. Please enter a numerical value for the budget amount.\n")
            return budget_intro()

    if amount <= 0:
            print("Please enter a valid budget amount greater than 0.\n")
            return budget_intro()
    elif amount > 1000000:
            print("That's a large budget! Please enter a more reasonable amount.\n")
            return budget_intro()
    else:
            return amount
    

budget_amount = budget_intro()

default_budget_allocation()
budget_allocation(budget_amount)

print("Do you want to follow this budget or would you like to change your budget allocation? \n"
      "yes or no")

# Follow-up Interaction
   