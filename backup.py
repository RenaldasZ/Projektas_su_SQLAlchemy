from typing import Any
from sqlalchemy import create_engine, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from datetime import datetime, date

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

def spausdinti(session):
    projektai = session.query(Projektas).all()
    print("-------------------")
    for projektas in projektai:
        print(projektas)
    print("-------------------")
    return projektai


while True:
    pasirinkimas = input("""Pasirinkite veiksmą: 
1 - atvaizduoti darbuotojus
2 - sukurti naują įrašą
3 - pakeisti darbuotojo duomenis
4 - ištrinti darbuotoją
0 - išeiti
>:""")

    try:
        pasirinkimas = int(pasirinkimas)
    except:
        pass

    if pasirinkimas == 1:
        projektai = spausdinti(session)

    elif pasirinkimas == 2:
        name = input("Įveskite darbuotojo vardą: ")
        last_name = input("Įveskite darbuotojo pavardę: ")
        birth_date = input("Įveskite gimimo datą (YYYY-MM-DD): ")
        position = input("Įveskite darbuotojo pareigas: ")
        salary = float(input("Įveskite darbuotojo atlyginimą: "))
        projektas = Projektas(name=name, last_name=last_name, birth_date=birth_date, position=position, salary=salary)
        session.add(projektas)
        session.commit()

    elif pasirinkimas == 3:
        projektai = spausdinti(session)
        try:
            keiciamas_id = int(input("Pasirinkite norimo pakeisti projekto ID: "))
            # keiciamas_projektas = session.get(Projektas, keiciamas_id)
            keiciamas_projektas = session.query(Projektas).filter_by(id=keiciamas_id).first()
        except Exception as e:
            print(f"Klaida: {e}")
        else:
            pakeitimas = int(input("Ką norite pakeisti: 1 - vardą, 2 - pavardę, 3 - gimimo datą, 4 - pareigą, 5 - atlyginimą "))
            if pakeitimas == 1:
                keiciamas_projektas.name = input("Įveskite darbuotojo vardą: ")
            if pakeitimas == 2:
                keiciamas_projektas.last_name = input("Įveskite darbuotojo pavardę: ")
            if pakeitimas == 3:
                ivesta_data = input("Įveskite darbuotojo gimimo datą(YYYY-MM-DD): ")
                keiciamas_projektas.birth_date = datetime.strptime(ivesta_data, '%Y-%m-%d')
            if pakeitimas == 4:
                keiciamas_projektas.position = input("Įveskite darbuotojo pareigas: ")
            if pakeitimas == 5:
                keiciamas_projektas.salary = float(input("Įveskite darbuotojo atlyginimą: "))
            session.commit()

    elif pasirinkimas == 4:
        projektai = spausdinti(session)
        trinamas_id = int(input("Pasirinkite norimo ištrinti projekto ID: "))
        try:
            trinamas_projektas = session.query(Projektas).filter_by(id=trinamas_id).first()
            # trinamas_projektas = session.get(Projektas, trinamas_id)
            session.delete(trinamas_projektas)
            session.commit()
        except Exception as e:
            print(f"Klaida: {e}")

    elif pasirinkimas == 0:
        print("Ačiū už tvarkingą uždarymą")
        break

    else:
        print("Klaida: Neteisingas pasirinkimas")

