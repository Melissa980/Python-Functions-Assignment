
#Question 2  Task 1
def add_to_shopping_list(shopping_list):
    item = input("Enter the item to add to the shopping list (or type 'done' to finish): ")
    while item.lower() != 'done':
        shopping_list.append(item)
        item = input("Enter the next item (or type 'done' to finish): ")

#Question 2  Task 2
def remove_from_shopping_list(shopping_list):
    item_to_remove = input("Enter the item to remove from the shopping list: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from the shopping list.")
    else:
        print("Item not found in the shopping list.")

#Question 2 Task 3
def print_shopping_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")

def main():
    shopping_list = []
    while True:
        print("1. Add items to the shopping list")
        print("2. Remove items from the shopping list")
        print("3. Print the shopping list")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_to_shopping_list(shopping_list)
        elif choice == '2':
            remove_from_shopping_list(shopping_list)
        elif choice == '3':
            print_shopping_list(shopping_list)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()