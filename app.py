import logging
import PySimpleGUI as sg
from Darbuotojai import show_employees_info, add_employee, edit_employee, delete_employee

# Configure logging
logging.basicConfig(filename='workers.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

sg.theme('DarkBrown7')  # Change the color scheme of the GUI
icon = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAFZklEQVR4nO3TWWxUVRwG8O/uc2fuLHfaKVO6sJRpS9kKCaCCpfKgDSYgEhAe5IFggEBCxKAPJmhifFDiEhMxmAiGKE0KYtkiLpVVC1ikmEKhWKaddtrZp7PfO3fuPT6ZGFMYEHzjez7n/8v3zznA4zxkurq6uLa2NqbYOfpRwz3e2MrBUKjyf4WPXiHT9nUSDwD0EMJvPtBdZhikRWKECcXuUg8CEUKoQ4dAr1lD6XsGiez9dWij79bNpYGRQFJN6rPURLB0xiTW/uRc8aWtm7a232sW+yDwmYEBYd3aKcrO44qn/aNf2hP+voZE2ItEMAJGV8ExLGJSFUIjqYnFZj3Qqt/ZdqTkuc0dTT3nez7PJvQGomlIBOPIp8MwOECnbdBZe2L58qaTxWbdd+Ol6z+rcNU3HxRFqSmvqpjvimCoK4asJCMGAoMRoGo88pSUnTpvaeKRwEveOs1Wy+59DjPVpIe6MTLqRerCEbzIOkBbZ6IDTuS1JAxKRcjvFbZs3y4Um3lfqz7zdrOuZ0ePnv5iGw5+shlnvvkAt/N5vMvkICl9eAIJOCQ7CnoODqfMrlj1Cv9IGgPgqhgy+zotYUF1IyizBSboGE5H4OEkaLoGJ0sjKdpBURTNWMxFf0tR+PUDt596df/ge4oqLG6c1Qw6mUTs0jHIsg01mgICDXYtAX4si4RjBnjRQu6nyT3h9suJuhOXA8f7e286x66cRq1FgdlIob5ERlkmBcFUBo/ZjE5UYYhQoEgBPG8CJwhF8bvCbRdHpwz5BltrZcUp1MgY7HViphBBlMrjiuFEuTgZDsrAgGBBi5HGMakOejYPo6BBfJjGF08dWtDbNzaX0kZRUdeCaj0OcWwAE/NxZLgJqOYUiDSFQC6BOxqPWfQIKiQ3AnYbcrncf4cjkaAjm9FgM7Pw9Q8gMHQDfyh+iI5yeKwaJqgZmDgBQ9IkDCpWeKwWKKwJajZDcwxT9LeMC7cFiXR231cb9Du/g+VYgJhhnToPhG/E9OwohPBVXFSACCVAEjX0spW4UcjBEDTIui3w/Lwp/i1vfvqsPxqpX7R91/43plOpfxvjPvvXdn+/MDR89aKvPwC3W0BlzVxkwsNIKRyun/0O3ddPweysgXtKHWrqaxEZiUJNByCXuCBI5SOBaObl7FDnzplV81vslrJrllmNe8Nq2jJ8Z/jmb+27Tty18fR5jbWVk2V4akMQeAZ1DbPR8ZMXP5/8EVDCaFqxAdcu/IAJNjPWLm9GnzeIwxf8CHIiBN46seCiOkrKajEjEsa1vnNzjArsEfkqRPvPh9ft2NvQ+uGmyLgwC2ZSy7L54HQABChoBO2tZ0HnvJDdpWheuRFBby/cLieqnDyycWD9CwvhqvYgHo1CVTVAEOA7cgxGRsBYyIesqqBcLjgHrhxzAxgf7jj8rUii5eCgwCSaEAoE0XP5FLRcCC67DTPKCRwOG7xDOjq7Y/D7o7h06RwEQQBL5cCyNMwWE4yICloug0mSEYmnUDm5Fn9e7aLuuuquC50h/x0NqWQKgACKqAgH0wZN03Q44Ec66EM8Fk7HYvTw11+2mlLxCKcaToHQdGn1VAk8xUBJ5pHOjMHK0Ih6Y/D130Kp82mSzWaN8UwAQF3dTmv9zMVLRNHaT1ECYVmpw+Va0lg5ccEGm10m8xc9Q0rLyt9fvbqB3717t8XpnGYTgBqapmIACMMwgwJvIqIokbLKaaTEPUkRzWZS4WmMW63Wkru+6r/jcDiWZDKJZQBp1TR0A4As23ckk+lKm832cTwe9/3zvCRJq1RVncPzOGwy2ZYBhljIF3iaxXmG4epy6ZQ/o2ht9zIf53EeOn8BWy1K8ndljBwAAAAASUVORK5CYII='

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
    [sg.Button('Exit', key='exit', size=(70, 1))],
    [sg.Text('', size=(70, 2), key='output')],
]

window = sg.Window('Workers database', layout, icon=icon,)


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
    
    elif event == 'edit':
        text = [values['name'], values['last_name'], values['birth_date'], values['position'], float(values['salary'])]
        edit_employee(values["change_id"], text)
        logging.info(f"User edited worker with ID {values['change_id']}: {text}")

    elif event == 'delete':
        delete_employee(values)
        logging.info(f"User deleted worker with ID {values['delete_id']}")
        
if __name__ == "__main__":
    window.close()

