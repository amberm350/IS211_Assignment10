import sqlite3


DB_PATH = "pets.db"

con = sqlite3.connect('pets.db')
cur = con.cursor()

PERSON_QRY = 'SELECT * FROM person'
PETS_QRY = 'SELECT * FROM pets' 
 


def main():
    
    id = int(input("Enter a person id? "))
    while id > 0:
        cur.execute(PERSON_QRY, (id))
        row = cur.fetchone()
        if row:
            print(f"first_name, last_name = {row[0]} {row[1]} / age = {row[2]}")
            cur.execute(PETS_QRY, (id))
            for row in cur.fetchall():
                print(f"name = {row[1]} / breed  = {row[2]} / age = {row[3]} / dead = {row[4]}")
            
        else:
            print(f"No people found with id = {id}")

        id = int(input("Enter a person id? "))

if __name__ == "__main__":
    main()