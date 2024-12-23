import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkGreen6")

clock = sg.Text('', key='clock')
space = sg.Text('                            ', key='space')
label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('ToDo App',
                   layout=[[label, space, clock],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please Select an Item First", font=('Helvetica', 14))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please Select an Item First", font=('Helvetica', 14))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()