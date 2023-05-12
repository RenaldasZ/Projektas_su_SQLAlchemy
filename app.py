
import logging
import PySimpleGUI as sg
from Darbuotojai import show_employees_info, add_employee, edit_employee, delete_employee, get_employees_info

# Configure logging
logging.basicConfig(filename='workers.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

sg.theme('DarkBrown7')  # Change the color scheme of the GUI

layout = [
    [sg.TabGroup([[sg.Tab('Workers Database', [
        [sg.Text('What would you like to do with the workers database?')],
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
        [sg.Listbox(values=[], key='database_list', size=(70, 5))],  # Add 'values=[]'
        [sg.Button('update info', key='get', size=(70, 1))], 
        [sg.Button('Edit worker information', key='edit', size=(70, 1))],
        [sg.Text('')],
        # Delete worker layout
        [sg.Text('Select the ID of the worker you want to delete: '), sg.InputText(key='delete_id', size=(30, 1))],
        [sg.Button('Delete worker', key='delete', size=(70, 1))],
        [sg.Button('Exit', key='exit', size=(70, 1))],
        [sg.Text('', size=(70, 2), key='output')],
    ])], [sg.Tab('Log', [
        [sg.Multiline('', key='log_output', size=(80, 15), disabled=True)],
    ])]])],
]

window = sg.Window('Workers database', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'exit':
        break

    elif event == 'show':
        show_employees_info()
        logging.info('User requested to show all workers')

    elif event == 'add':
        add_employee(values)
        logging.info(f"User added a new worker: {values['name']} {values['last_name']}")

    elif event == 'get':
        employees = get_employees_info()
        employee_values = []  # List to store employee information for Listbox
        for employee in employees:
            employee_info = f"ID: {employee.id}, Name: {employee.name}, Last Name: {employee.last_name}, Birth Date: {employee.birth_date}, Position: {employee.position}, Salary: {employee.salary}$"
            employee_values.append(employee_info)
        window['database_list'].update(values=employee_values)
        logging.info('User requested to show all workers')

    elif event == 'edit':
        text = [values['name'], values['last_name'], values['birth_date'], values['position'], float(values['salary'])]
        edit_employee(values["change_id"], text)
        logging.info(f"User edited worker with ID {values['change_id']}: {text}")

    elif event == 'delete':
        delete_employee(values)
        logging.info(f"User deleted worker with ID {values['delete_id']}")

    # Display logs in the log_output element
    with open('workers.log', 'r') as file:
        logs = file.read()
        window['log_output'].update(logs)
        
if __name__ == "__main__":
    window.close()

