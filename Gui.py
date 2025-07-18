import Functions
import FreeSimpleGUI as fsg

lable =fsg.Text("Type in  Todo ")
input_box = fsg.InputText(tooltip =" ADD A TODO",key='todo')
add_button =fsg.Button("Add")
window = fsg.Window("Todo List App",
                    layout =[[lable],[input_box,add_button]],
                    font=("Helvetica",20))
while True:
    event, values =window.read()
    match event:
        case "Add":
            todos =Functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
        case fsg.WINDOW_CLOSED:
            break

window.close()









window.close()