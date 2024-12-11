# from functions import get_todos, write_todos
from modules import functions
import time
print("                                        ")
now = time.strftime("%H:%M:%S on %b %d, %Y")
print("The time is now:", now)
print("                                        ")
print(" *  **  **  *** ********* ***  **  **  *")
print(" *  **  **  *** ToDo List ***  **  **  *")
print(" *  **  **  *** ********* ***  **  **  *")
print("                                        ")
while True:
    user_action = input('Type add, show, edit, complete, or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}: {item}"
            print(row)
        print(f"There are {len(todos)} todos on the list")

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Invalid Command; Type add, show, edit, complete, or exit: ")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)
            functions.write_todos(todos)
            message = f"Todo: {todo_to_remove}, was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid Command: Try add, show, edit, complete or exit")
print('Be seeing you!')