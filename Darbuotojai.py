from datetime import datetime
import PySimpleGUI as sg
from config import Projektas, session
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime


def show_employees_info():
    """
    Displays a popup message with information about all employees retrieved from the database.

    Parameters:
    None

    Returns:
    None
    """
    # Get all employees from the database
    employees = session.query(Projektas).all()
    
    # Initialize a string to store employee information
    employee_info = ""

    # Loop through each employee and append their information to the employee_info string (Used list comprehension to simplify the code Instead of using a for loop to iterate through each employee)
    employee_info = "\n".join([f"\nID: {employee.id} \nName: {employee.name}\nLast Name: {employee.last_name}\nBirth Date: {employee.birth_date}\nPosition: {employee.position}\nSalary: {employee.salary}$\n" for employee in employees])

    # Display a popup message with the number of retrieved employees and their information
    sg.popup(f"Workers information\nRetrieved {len(employees)} employees from the database:{employee_info}")


def add_employee(values):
    try:
        name = values['name']
        last_name = values['last_name']
        birth_date = values['birth_date']
        position = values['position']
        salary = values['salary']
    except KeyError as e:
        sg.popup(f"Error: the key {e} is missing from the values provided.")
        return
    try:
        employee = Projektas(name=name, last_name=last_name, birth_date=birth_date, position=position, salary=salary)
        session.add(employee)
        session.commit()
        sg.popup(f"{name} {last_name} has been added to the database.")
    except Exception as e:
        sg.popup(f"Error: failed to add employee. {e}")

def delete_employee(values):
    employee_id = int(values['delete_id'])
    employee = session.query(Projektas).get(employee_id)
    if employee:
        session.delete(employee)
        session.commit()
        sg.popup(f'Darbuotojas su ID {employee_id} buvo ištrintas iš duomenų bazės.')
    else:
        sg.popup(f'Nepavyko rasti darbuotojo su ID {employee_id}.')


def edit_employee(el_id, emp_list):
    try:
        darbuotojas = session.query(Projektas).filter(Projektas.id.like(f"{el_id}")).one()
        darbuotojas.name = emp_list[0]
        darbuotojas.last_name = emp_list[1]
        darbuotojas.birth_date = datetime.strptime(emp_list[2], '%Y-%m-%d').date()
        darbuotojas.position = emp_list[3]
        darbuotojas.salary = emp_list[4]
        session.commit()
        print(darbuotojas)
    except NoResultFound:
        sg.popup(f"Error: Employee with ID {el_id} not found.")
    except (IndexError, ValueError):
        sg.popup("Error: Invalid input format.")
    except Exception as e:
        sg.popup(f"Error: {str(e)}")
        session.rollback()


