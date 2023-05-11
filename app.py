import PySimpleGUI as sg
from Darbuotojai import show_employees_info, add_employee, atnaujinti_elementa, delete_employee

sg.theme('DarkBrown7')  # Change the color scheme of the GUI

# GUI Layout 
layout = [    [sg.Text('What would you like to do with the workers database?')],
    [sg.Button('Show all workers from the database', key='show', size=(70, 1))],
    [sg.Text('')],

# Create worker layout
    [sg.Text('Enter the worker\'s name: '), sg.InputText(key='name', size=(30, 1))],
    [sg.Text('Enter the worker\'s last name: '), sg.InputText(key='last_name', size=(30, 1))],
    [sg.Text('Enter the worker\'s birth date (YYYY-MM-DD): '), sg.InputText(key='birth_date', size=(30, 1))],
    [sg.Text('Enter the worker\'s position: '), sg.InputText(key='position', size=(30, 1))],
    [sg.Text('Enter the worker\'s salary: '), sg.InputText(key='salary', size=(30, 1))],
    [sg.Button('Create a new record', key='add', size=(70, 1))],
    [sg.Text('')],

# Edit worker layout
    [sg.Text('Select the ID of the worker you want to edit: '), sg.InputText(key='change_id', size=(30, 1))],
    [sg.Button('Edit worker information', key='edit', size=(70, 1))],
    [sg.Text('')],

# Delete worker layout
    [sg.Text('Select the ID of the worker you want to delete: '), sg.InputText(key='delete_id', size=(30, 1))],
    [sg.Button('Delete worker', key='delete', size=(70, 1))],
    [sg.Button('Exit', key='0', size=(70, 1))],
    [sg.Text('', size=(70, 2), key='output')],
]

window = sg.Window('Workers database', layout)


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == '0':
        break

    elif event == 'show':
        show_employees_info()

    elif event == 'add':
        add_employee(values)
    
    elif event == 'edit':
        text = [values['name'], values['last_name'], values['birth_date'], values['position'], float(values['salary'])]
        atnaujinti_elementa(values["change_id"], text)

    elif event == 'istrinti':
        delete_employee(values)
        
if __name__ == "__main__":
    window.close()

