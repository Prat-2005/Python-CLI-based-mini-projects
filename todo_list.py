# Simple To-Do List App

def add_task(lim = 1):
    for _ in range(lim):
        insert_task = input("Enter task:")
        if insert_task == "":
            raise ValueError("Empty field! Please enter your task")
        
        tasks.append(insert_task.capitalize())
        print(f"\"{insert_task}\" added successfully.\n")
    
def view_tasks():
    print("To-Do List:")
    for idx in range(len(tasks)):
        print(f"{idx + 1}. {tasks[idx]}")

def delete_task(target_idx):
    delete_task = tasks.pop(target_idx)
    return delete_task
        

try:
    lim = int(input("How many tasks you want to enter?:"))
    tasks = []
    ch = 0
    print("To-Do List Created. Entering your tasks...")
    add_task(lim)

    while ch != 4:
        print("Choose what do you like to modify?")
        print("1. Add task")
        print("2. View task")
        print("3. delete task")
        print("4. Exit")

        ch = int(input("Enter your choice:"))

        if ch == 1:
            print("Adding one more task into your to-do list...")
            add_task()
        elif ch == 2:
            print("Viewing your tasks...")
            view_tasks()
            print()
        elif ch == 3:
            target = int(input("Enter the task's index which you want to remove:"))
            if target < 1 or target > len(tasks):
                raise IndexError("Index out of range! Please enter valid index")

            print("Removing one task from your to-do list...")
            print(f"{delete_task(target - 1)} deleted successfully.\n")
        elif ch == 4:
            print("Exiting...")
        else:
            print("Invalid input! Please enter valid input(1 - 3).")
    
except IndexError as e:
    print(f"An error occured: {e}.")
except ValueError as e:
    print(f"An error occured: {e}.")