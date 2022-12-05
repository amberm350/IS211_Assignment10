import sqlite3

def add_person_table():

    person = (
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    )

    con = sqlite3.connect('pets.db')

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS person")
        cur.execute("CREATE TABLE Person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
        cur.executemany("INSERT INTO Person VALUES(?, ?, ?, ?)", person)
        
def add_pets_table():

    pets = (
(1,'Rusty','Dalmation',4,1),
(2,'Bella','AlaskanMalamute',3,0),
(3,'Max','CockerSpaniel',1,0),
(4,'Rocky','Beagle',7,0),
(5,'Rufus','CockerSpaniel',1,0),
(6,'Spot','Bloodhound',2,1)
    )

    con = sqlite3.connect('pets.db')

    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS pets")
        cur.execute("CREATE TABLE pets(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, age TEXT, dead INTEGER)")
        cur.executemany("INSERT INTO pets VALUES(?, ?, ?, ?, ?)", pets)
        
if __name__ == '__main__':
    add_pets_table()

def add_person_pet_table():

    con = sqlite3.connect('pets.db')

    person_pet = [
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(4, 6)
    ]
    with con:
        cur = con.cursor()

        cur.execute("DROP TABLE IF EXISTS person_pet")
        cur.execute("CREATE TABLE person_pet(person_id INTEGER, pet_id INTEGER)")
        cur.executemany("INSERT INTO person_pet VALUES(?, ?)", person_pet)
        
if __name__ == '__main__':
    add_person_pet_table()

    


    


    