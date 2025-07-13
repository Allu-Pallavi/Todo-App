FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads the text file and show the todo list"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return  todos_local # here it returns values which is stored in todos_local


def write_todos(todos_local,filepath=FILEPATH):
    """ Opens the text file and modifies in the todo list"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)
if __name__=="__main__":
    print(get_todos())