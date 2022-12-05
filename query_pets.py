import sqlite3

DB_PATH = "pets.db"

con = sqlite3.connect('pets.db')
cur = con.cursor()

PERSON_QRY = 'SELECT * FROM person'
PETS_QRY = 'SELECT * FROM pets' 
PERSON_PET_QRY = 'SELECT * FROM person_pet'


def main():
    
    id = int(input("Enter a person id? "))
    
    while id > 0:
        cur.execute(PERSON_PET_QRY)
        for row in cur.fetchall(): 
            print (row[0], row[1])
        cur.execute(PERSON_QRY)
        row = cur.fetchone()
        if row:
            print(f"ID = {row[0]} / first_name = {row[1]} / last_name = { row[2]} / age = {row[3]}")
            cur.execute(PETS_QRY)
            for row in cur.fetchall():
                print(f"ID = {row[0]} / name = {row[1]} / breed = {row[2]} / age = {row[3]} / dead = {row[4]}")
        else:
            print(f"No people found with id = {id}")

        id = int(input("Enter a person id? "))

if __name__ == "__main__":
    main()