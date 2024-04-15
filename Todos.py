from functions import read_todos, write_todos


print("Welcome to the TO-DO App. ")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        # 'with' context manager is better for file handling than this block of code
        todos = read_todos()

        todos.append(todo + "\n")
        # file = open("todos.txt", "w")
        # file.writelines(todos)
        # file.close()
        # replaced this block of code with "with" context manager
        write_todos(todos)



    elif user_action.startswith("show"):
        # file = open("todos.txt", "r")
        # todos = file.readlines()
        # file.close()
        # replaced with 'with' context manager
        todos = read_todos()
        # print(todos)
        # new_todo = [item.strip("\n") for item in todos]
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            # print(index + 1, "-", item)
            print(row)

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            # with open("todos.txt", 'r') as file:
            #     todos = file.readlines()
            # replaced by function call to keep the code DRY
            todos = read_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("That command is not valid!")
            continue

    elif user_action.startswith("complete"):

        try:
            todos = read_todos()

            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            message = f"The todo '{todo_to_remove}' has been removed from the list"
            print(message)

            write_todos(todos)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")

print("Bye! Bye! See you later!")
