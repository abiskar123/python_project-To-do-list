todo_list=[]

def add_task():
    task=input("enter the task: ")
    todo_list.append({"Task":task,"status":"pending"})
    print("New task added successfully\n")


def  view_task():
    print("your todo List")
    if(len(todo_list)==0):
        print("No task is pending")
    else:
        for index,task in enumerate(todo_list,1):
            print(f"{index}:{task["Task"]}-{task['status']}")
    print('\n')


def remove_task():
    if(len(todo_list)==0):
        print('list is empty')
    else:
        try:
            search_index=int(input("enter the task that you waant to remove: "))-1
            if 0<=search_index<len(todo_list):
                remove_task=todo_list.pop(search_index)
                print(f"Task Removed: {remove_task['Task']}")
            else:
                print("Invalid Task Number")

        except ValueError:
            print("please enter the valid Task Number")
       

def mark_done():
    if(len(todo_list)==0):
        print('list is empty')
    else:
        try:
            search_index=int(input("enter the task that you waant to remove: "))-1
            if 0<=search_index<len(todo_list):
               todo_list[search_index]['status']='done'
               print(f"Task { todo_list[search_index]['Task']} has been marked as Done :")
            else:
                print("Invalid Task Number")

        except ValueError:
            print("please enter the valid Task Number")

def exit():
    print("Application exited")

#function to display menu
def menu():
    while True:
        print("***main menu***")
        print("1. Add a new Task")
        print("2. view all Task ")
        print("3. Remove a Task")
        print("4. Mark a task as completed")
        print("5. Exit")

        choice=input("Enter the choice: ")
        match choice:
            case "1":
                add_task()
            case "2":
                view_task()
            case "3":
                remove_task()
            case "4":
                mark_done()
            case "5":
                print("Exiting the application")
                exit()
            case "_":
                print("invalid choice :Try Again")


menu()