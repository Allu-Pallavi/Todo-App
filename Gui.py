import Functions
import FreeSimpleGUI  as fsg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as file:
        pass

fsg.theme("Black")

clock = fsg.Text(" ",key = "clock")
label = fsg.Text("Type in a Todo")
input_box = fsg.InputText(tooltip="Add a todo", key='todo')
add_button = fsg.Button("Add")
complete_button = fsg.Button("Complete")
list_box = fsg.Listbox(values=Functions.get_todos(), key='todos',
                       enable_events=True,
                       size=[45, 10])
edit_button = fsg.Button("Edit")
exit_button = fsg.Button("Exit")

window = fsg.Window("Todo List App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d %b-%Y,%H:%M:%S"))

    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = Functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                Functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select a todo to edit.")

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = Functions.get_todos()
                todos.remove(todo_to_complete)
                Functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                fsg.popup("Please select a todo to complete.")

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case fsg.WINDOW_CLOSED:
            break

window.close()
