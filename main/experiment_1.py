import sqlite3


class Person(object):
    def __init__(self, id_number: int = -1, first_name: str = '', last_name: str = '', age: int = -1) -> None:
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        ) 
        """)

    def insert_person(self) -> None:
        self.cursor.execute("""
        INSERT INTO persons VALUES
        ({}, '{}', '{}', {})
        """.format(self.id_number, self.first_name, self.last_name, self.age))
        self.connection.commit()

    def load_person(self, id_number: int) -> None:
        # Implementar tupla nomeada
        self.cursor.execute("""
        SELECT * FROM persons
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first_name = results[1]
        self.last_name = results[2]
        self.age = results[3]


p1 = Person(1, 'Alex', 'Smith', 32)
p1.insert_person()
p2 = Person(2, 'Anna', 'John', 43)
p2.insert_person()

p = Person()
p.load_person(1)
print(p.id_number)
print(p.first_name)
print(p.last_name)
print(p.age)
p.load_person(2)
print(p.id_number)
print(p.first_name)
print(p.last_name)
print(p.age)
