import sqlite3

DB_PATH = "pets.db"

sql = "INSERT INTO person (id, first_name, last_name, age) VALUES (%s, %s, %s, %s)"

Val1= [
(1, 'James', 'Smith', 41),
(2,'Diana','Greene',23),
(3,'Sara','White',27),
(4,'William','Gibson',23)
]

sql = "INSERT INTO pet (id, name, breed, age, dead) VALUES (%s, %s, %s, %s, %s)"

Val2= [
(1,'Rusty','Dalmation',4,1),
(2,'Bella','AlaskanMalamute',3,0),
(3,'Max','CockerSpaniel',1,0),
(4,'Rocky','Beagle',7,0),
(5,'Rufus','CockerSpaniel',1,0),
(6,'Spot','Bloodhound',2,1)
]

sql = "INSERT INTO person_pet (person_id, pet_id) VALUES (%s, %s)"

Val3= [
(1,1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(4, 6)
]

    


    


    