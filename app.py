# Functions
def menu():
    print("\n")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Tasks as Complete")
    print("4. Exit")

# Welcome Screen
print("==== TO DO LIST APP ====")

tasklist = {}
tasknum = 0

while (True):
    menu()
    choice = int(input("Enter Choice: "))

    # Option 1
    if (choice == 1):
        task = input("Enter Task: ")
        tasknum += 1
        tasklist[tasknum] = task

    elif (choice == 2):
        for key, value in tasklist.items():
            print(key, ":", value)
    
    elif (choice == 3):
        completed = int(input("Completed Task Number: "))
        tasklist.pop(completed)
        for key, value in tasklist.items():
            print(key, ":", value)
    
    else:
        break

    



