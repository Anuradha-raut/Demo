# To-Do list
tasks=[]
while True:
    print("\n------To-Do-list------")
    print("1. Add tasks")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete tasks")
    print("5. Exit the program")

    choice=input("Enter your choice:")

    if choice =='1':
        n_tasks=int(input("Enter how many tasks you want to added:"))
        for i in range(n_tasks):
            task=input("Enter the task:")
            tasks.append({"task":task , "done":False})
            print("Task added!")

    elif choice =='2':
           print("\nTasks:")
           for index, task in enumerate(tasks):
               status="Done" if task["done"] else "not done"
               print(f" {index+1}.{task['task']} - {status}")

    elif choice =='3':
        task_index=int(input("Enter the task number to mark as done:"))
        if 0< task_index <= len(tasks):
            print("Task marked as done")
        else:
            print("Invalid task number")

    elif choice=='4':
        task_name=input("Enter the task name to delete:")
        del(tasks)

        print("tasks are deleted successfully")

    elif choice=='5':
        print("Exiting the To-Do list")
        break

    else:
        print("Invalid choice, please try again")