def read_todos():
    """ Read a text file and return a list of
    to-do items.
    """
    with open("todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todo_arg, filepath="todos.txt"):
    """ Write the to-do items in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)