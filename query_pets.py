import sqlite3

DB_PATH = "pets.db"

con = sqlite3.connect('pets.db')
cur = con.cursor()

def main():
    
    id = int(input("Enter a person id? "))

    query = f"select p.first_name, p.last_name, p.age, t.name, t.breed, t.age FROM person p inner join person_pet pp on p.id = pp.person_id inner join pets t on pp.pet_id = t.id where p.id = {id}"

    while id > 0:
        cur.execute(query.format(id))
        for row in cur.fetchall():
            if row:
                print(row)

            else:
                print(f"No people found with id = {id}")

            
        
        

if __name__ == "__main__":
    main()