from db_config import Base, engine
import tables # Importujemy wszystkie modele

# Tworzymy tabele
Base.metadata.create_all(bind=engine)

print("Baza danych i tabele zostały utworzone!")
