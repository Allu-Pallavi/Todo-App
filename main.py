print("Welcome to the ToDo App")
import Functions
import time
now = time.strftime("%d %b-%Y,%H:%S:%M")
print(now)
while True:
    user_action=input("Enter add, show, edit,complete or exit :\n")
    user_action= user_action.strip()

    if  user_action.startswith("add"):
        todo= user_action[4:]        #todo=input(enter a todo)

        todos=Functions.get_todos()   # default arugment # is get_todo(".txt") we are calling a function (get_todos) for read mode and storing in a global variable


        todos.append(todo +'\n')

        Functions.write_todos(todos)


    elif  user_action.startswith("show"):
        todos = Functions.get_todos()  # filepath=todos.txt

        for index,item in enumerate(todos):
            item=item.strip('\n')
            item = item.title()
            print(f"{index+1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number =int(user_action[5:]) # or number= int(input(enter a number to edit))
            number = number -1
            todos = Functions.get_todos("todos.txt") #filepath=todos.txt

            todos[number]=input("enter a new todo") +'\n'  #or new_todo=input("enter a new") +'\n
                                                     #todos[number]=new_todo
            Functions.write_todos(todos)

        except ValueError:
            print("hey u command is invalid give the todo number  for which you want to edit")
            continue


    elif  user_action.startswith("complete"):
        try:
            numbers = int(user_action[9:])                      #int(input("enter a number which you completed:"))
            numbers = numbers -1

            todos = Functions.get_todos() #filepath=todos.txt

            todos.pop(numbers)

            Functions.write_todos(todos)
        except TypeError:
            print("Your command does not have an number in this todo enter the number which is present in these todos")
            continue

    elif   user_action.startswith("exit"):
        break
    else :
        print("hey you entered something invalid")
print("Bye")




