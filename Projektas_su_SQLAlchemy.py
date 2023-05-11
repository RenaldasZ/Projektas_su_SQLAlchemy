from typing import Any
from sqlalchemy import create_engine, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from datetime import datetime
import PySimpleGUI as sg

engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass


class Projektas(Base):
    __tablename__ = "projektas"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(50), nullable=False)
    last_name = mapped_column(String(50), nullable=False)
    birth_date = mapped_column(Date, nullable=False)
    position = mapped_column(String(50), nullable=False)
    salary = mapped_column(Float(2), nullable=False)
    work_since = mapped_column(DateTime, default=datetime.utcnow)

    def __init__(self, **kw: Any):
        # super().__init__(**kw)
        for key, value in kw.items():
            if key == 'birth_date':
                value = datetime.strptime(value, '%Y-%m-%d')
            setattr(self, key, value)
    
    def __repr__(self) -> str:
        return f"({self.id}, {self.name}, {self.last_name}, {self.birth_date}, {self.position}, {self.salary}, {self.work_since})"

Base.metadata.create_all(engine)

# def spausdinti(session):
#     projektai = session.query(Projektas).all()
#     print("-------------------")
#     for projektas in projektai:
#         print(projektas)
#     print("-------------------")
#     return projektai


def show_employees():
    # Get all employees from the database
    employees = session.query(Projektas).all()
    
    # Initialize a string to store employee information
    employee_info = ""

    # Loop through each employee and append their information to the employee_info string
    for employee in employees:
        employee_info += f"\nId: {employee.id} \nName: {employee.name}\nLast Name: {employee.last_name}\nBirth Date: {employee.birth_date}\nPosition: {employee.position}\nSalary: {employee.salary}$\n"

    # Display a popup message with the number of retrieved employees and their information
    sg.popup(f"Retrieved {len(employees)} employees from the database:{employee_info}")


def add_employee(values):
    name = values['name']
    last_name = values['last_name']
    birth_date = values['birth_date']
    position = values['position']
    salary = values['salary']
    darbuotojas = Projektas(name=name, last_name=last_name, birth_date=birth_date, position=position, salary=salary)
    session.add(darbuotojas)
    session.commit()
    sg.popup(f"{name} {last_name} buvo pridėtas prie duomenų bazės.")

def delete_employee(values):
    employee_id = int(values['delete_id'])
    employee = session.query(Projektas).get(employee_id)
    if employee:
        session.delete(employee)
        session.commit()
        sg.popup(f'Darbuotojas su ID {employee_id} buvo ištrintas iš duomenų bazės.')
    else:
        sg.popup(f'Nepavyko rasti darbuotojo su ID {employee_id}.')

def atnaujinti_elementa(el_id, list):
        session = Session(bind=engine)
        darbuotojas = session.query(Projektas).filter(Projektas.id.like(f"{el_id}")).one()
        darbuotojas.name = list[0]
        darbuotojas.last_name = list[1]
        darbuotojas.birth_date = datetime.strptime(list[2], '%Y-%m-%d').date()
        darbuotojas.position = list[3]
        darbuotojas.salary = list[4]
        session.commit()
        print(darbuotojas)
# if __name__ == "__main__":



    # while True:
    #     pasirinkimas = input("""Pasirinkite veiksmą: 
    # 1 - atvaizduoti darbuotojus
    # 2 - sukurti naują įrašą
    # 3 - pakeisti darbuotojo duomenis
    # 4 - ištrinti darbuotoją
    # 0 - išeiti
    # >:""")

    #     try:
    #         pasirinkimas = int(pasirinkimas)
    #     except:
    #         pass

    #     if pasirinkimas == 1:
    #         projektai = spausdinti(session)

    #     elif pasirinkimas == 2:
    #         name = input("Įveskite darbuotojo vardą: ")
    #         last_name = input("Įveskite darbuotojo pavardę: ")
    #         birth_date = input("Įveskite gimimo datą (YYYY-MM-DD): ")
    #         position = input("Įveskite darbuotojo pareigas: ")
    #         salary = float(input("Įveskite darbuotojo atlyginimą: "))
    #         projektas = Projektas(name=name, last_name=last_name, birth_date=birth_date, position=position, salary=salary)
    #         session.add(projektas)
    #         session.commit()

    #     elif pasirinkimas == 3:
    #         projektai = spausdinti(session)
    #         try:
    #             keiciamas_id = int(input("Pasirinkite norimo pakeisti projekto ID: "))
    #             keiciamas_projektas = session.query(Projektas).filter_by(id=keiciamas_id).first()
    #         except Exception as e:
    #             print(f"Klaida: {e}")
    #         else:
    #             pakeitimas = int(input("Ką norite pakeisti: 1 - vardą, 2 - pavardę, 3 - gimimo datą, 4 - pareigą, 5 - atlyginimą "))
    #             if pakeitimas == 1:
    #                 keiciamas_projektas.name = input("Įveskite darbuotojo vardą: ")
    #             if pakeitimas == 2:
    #                 keiciamas_projektas.last_name = input("Įveskite darbuotojo pavardę: ")
    #             if pakeitimas == 3:
    #                 ivesta_data = input("Įveskite darbuotojo gimimo datą(YYYY-MM-DD): ")
    #                 keiciamas_projektas.birth_date = datetime.strptime(ivesta_data, '%Y-%m-%d')
    #             if pakeitimas == 4:
    #                 keiciamas_projektas.position = input("Įveskite darbuotojo pareigas: ")
    #             if pakeitimas == 5:
    #                 keiciamas_projektas.salary = float(input("Įveskite darbuotojo atlyginimą: "))
    #             session.commit()

    #     elif pasirinkimas == 4:
    #         projektai = spausdinti(session)
    #         trinamas_id = int(input("Pasirinkite norimo ištrinti projekto ID: "))
    #         try:
    #             trinamas_projektas = session.query(Projektas).filter_by(id=trinamas_id).first()
    #             session.delete(trinamas_projektas)
    #             session.commit()
    #         except Exception as e:
    #             print(f"Klaida: {e}")

    #     elif pasirinkimas == 0:
    #         print("Ačiū už tvarkingą uždarymą")
    #         break

    #     else:
    #         print("Klaida: Neteisingas pasirinkimas")
