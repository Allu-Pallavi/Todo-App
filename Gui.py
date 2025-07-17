import Functions
import FreeSimpleGUI as fsg

lable =fsg.Text("Type in  Todo ")
input_box = fsg.InputText(tooltip =" ADD A TODO")
add_button =fsg.Button("Add")
window = fsg.Window("Todo List App", layout =[[lable],[input_box,add_button]])
window.read()
window.close()