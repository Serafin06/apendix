from db_config import SessionLocal
from tables import Buildings

# Tworzymy sesję
session = SessionLocal()

# Dodajemy budynek
new_building = Buildings(address="Warszawa, ul. Przykładowa 10")
session.add(new_building)
session.commit()

print("Budynek dodany!")
