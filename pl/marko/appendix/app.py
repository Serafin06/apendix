import sys
import app
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from pl.marko.appendix.db_config import SessionLocal
from pl.marko.appendix.tables.buildings import Building
from pl.marko.appendix.tables.works import Work



class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zarządzanie Budynkami i Pracami")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Pola do dodania budynku
        self.address_label = QLabel("Adres budynku:")
        self.address_input = QLineEdit()
        self.add_building_btn = QPushButton("Dodaj budynek")
        self.add_building_btn.clicked.connect(self.add_building)

        # Pola do dodania pracy
        self.work_desc_label = QLabel("Opis pracy:")
        self.work_desc_input = QLineEdit()
        self.work_hours_label = QLabel("Ilość godzin:")
        self.work_hours_input = QLineEdit()
        self.work_building_label = QLabel("Adres budynku (dla pracy):")
        self.work_building_input = QLineEdit()
        self.add_work_btn = QPushButton("Dodaj pracę")
        self.add_work_btn.clicked.connect(self.add_work)

        # Dodajemy elementy do layoutu
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_input)
        layout.addWidget(self.add_building_btn)
        layout.addWidget(self.work_desc_label)
        layout.addWidget(self.work_desc_input)
        layout.addWidget(self.work_hours_label)
        layout.addWidget(self.work_hours_input)
        layout.addWidget(self.work_building_label)
        layout.addWidget(self.work_building_input)
        layout.addWidget(self.add_work_btn)

        self.setLayout(layout)

    def add_building(self):
        """Dodaje budynek do bazy danych"""
        session = SessionLocal()
        address = self.address_input.text()

        if not address:
            QMessageBox.warning(self, "Błąd", "Adres nie może być pusty!")
            return

        new_building = Building(address=address)
        session.add(new_building)
        session.commit()
        session.close()

        QMessageBox.information(self, "Sukces", f"Budynek '{address}' został dodany!")
        self.address_input.clear()

    def add_work(self):
        """Dodaje pracę do istniejącego budynku"""
        session = SessionLocal()
        address = self.work_building_input.text()
        description = self.work_desc_input.text()
        total_hours = self.work_hours_input.text()

        if not address or not description or not total_hours:
            QMessageBox.warning(self, "Błąd", "Wszystkie pola muszą być wypełnione!")
            return

        # Sprawdzenie czy budynek istnieje
        building = session.query(Building).filter_by(address=address).first()
        if not building:
            QMessageBox.warning(self, "Błąd", "Nie znaleziono budynku o podanym adresie!")
            return

        new_work = Work(
            building_id=building.id,
            description=description,
            total_hours=float(total_hours),
            travel_cost=0,  # Można dodać pole do wprowadzania kosztu dojazdu
            vat_rate=23.0  # Można dodać pole do VAT
        )
        session.add(new_work)
        session.commit()
        session.close()

        QMessageBox.information(self, "Sukces", "Praca została dodana!")
        self.work_desc_input.clear()
        self.work_hours_input.clear()
        self.work_building_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
