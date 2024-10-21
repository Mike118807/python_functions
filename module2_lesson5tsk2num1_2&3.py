# 2: The Shopping List Maker
# 
# Objective: The aim of this assignment is to create a program that helps users make a shopping list.
#
# Task 1: Write a function that lets the user add items to a list.
#
# Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, 
# and print off their shopping list until they decide to "quit", also known as breaking the loop.
#
# NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, 
# they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.

def add_item(shopping_list, item):

    shopping_list.append(item)

    print(f"'{item}' add to the shopping list.")


#  Task 2: Include a function to remove items from the list.
#


def remove_item(shopping_list, item):
    
    if item in shopping_list:
        
        shopping_list.remove(item)
        
        print(f"'{item}' remove from the shopping list. ")
    
    else: print(f"'{item}' not found in shopping list. ")



# Task 3: Add a function that prints out the entire list in a formatted way.
#


def print_list(shopping_list):
    
    if shopping_list:
        
        print("shopping List:")
        
        for i, item in enumerate(shopping_list, start=1):
            
            print(f"{i}. {item} ")
    
    else:
        print("The shopping list is empty.")
        

def main():
    shopping_list = []

    while True:
        print("\nOptions: 'add', 'remove', 'print', 'quit' ")

        choice = input("Enter the item to add: ").strip().lower()

        if choice == "add":
            item = input("Enter the item to add:").stip()
            add_item(shopping_list, item)

        elif choice == "remove":
            item = input("Enter the item to remove: ").strip()
            remove_item(shopping_list, item)

        elif choice == "print":
            print_list(shopping_list)

        elif choice == "quit":
            print("Exiting the shopping list maker. Goodbye for now! ")
            break
        else:
            print("Invalid choice. Try again. ")

if __name__ == "__main__":
    main()