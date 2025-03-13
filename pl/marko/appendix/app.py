import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class WorkEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dodawanie Pracy")
        self.root.geometry("800x600")

        self.frame1 = tk.Frame(root)
        self.frame2 = tk.Frame(root)
        self.frame3 = tk.Frame(root)
        self.frame4 = tk.Frame(root)
        self.frame5 = tk.Frame(root)

        self.create_address_date_frame()

    def create_address_date_frame(self):
        self.clear_frame()

        tk.Label(self.frame1, text="Adres").pack()
        self.address_entry = tk.Entry(self.frame1, width=50)
        self.address_entry.pack()

        tk.Label(self.frame1, text="Data").pack()
        self.date_entry = DateEntry(self.frame1, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.pack()

        tk.Button(self.frame1, text="Dalej", command=self.create_work_description_frame).pack()
        self.frame1.pack()

    def create_work_description_frame(self):
        self.clear_frame()

        tk.Label(self.frame2, text="Opis Wykonanej Pracy").pack()
        self.work_text = tk.Text(self.frame2, width=60, height=10)
        self.work_text.pack()

        tk.Button(self.frame2, text="Dalej", command=self.create_vat_material_frame).pack()
        self.frame2.pack()

    def create_vat_material_frame(self):
        self.clear_frame()

        tk.Label(self.frame3, text="Stawka VAT").pack()
        self.vat_var = tk.IntVar(value=8)
        tk.Radiobutton(self.frame3, text="8%", variable=self.vat_var, value=8).pack()
        tk.Radiobutton(self.frame3, text="23%", variable=self.vat_var, value=23).pack()

        tk.Label(self.frame3, text="Materiał").pack()
        self.material_var = tk.StringVar()
        self.material_combobox = ttk.Combobox(self.frame3, textvariable=self.material_var,
                                              values=["Cement", "Farba", "Drewno", "Gips"])
        self.material_combobox.pack()
        self.material_combobox.bind("<KeyRelease>", self.update_material_list)

        tk.Label(self.frame3, text="Jednostka Miary").pack()
        self.unit_label = tk.Label(self.frame3, text="")
        self.unit_label.pack()

        tk.Label(self.frame3, text="Ilość").pack()
        self.quantity_entry = tk.Entry(self.frame3)
        self.quantity_entry.insert(0, "1")
        self.quantity_entry.pack()

        tk.Button(self.frame3, text="Dalej", command=self.create_travel_preview_frame).pack()
        self.frame3.pack()

    def update_material_list(self, event):
        material_units = {"Cement": "kg", "Farba": "litr", "Drewno": "metr", "Gips": "kg"}
        material = self.material_var.get()
        self.unit_label.config(text=material_units.get(material, ""))

    def create_travel_preview_frame(self):
        self.clear_frame()

        self.travel_var = tk.BooleanVar()
        tk.Checkbutton(self.frame4, text="Dojazd", variable=self.travel_var).pack()

        tk.Button(self.frame4, text="Podgląd", command=self.create_summary_frame).pack()
        self.frame4.pack()

    def create_summary_frame(self):
        self.clear_frame()

        summary = f"Adres: {self.address_entry.get()}\n"
        summary += f"Data: {self.date_entry.get()}\n"
        summary += f"Praca: {self.work_text.get('1.0', tk.END).strip()}\n"
        summary += f"VAT: {self.vat_var.get()}%\n"
        summary += f"Materiał: {self.material_var.get()} ({self.unit_label.cget('text')}) x {self.quantity_entry.get()}\n"
        summary += f"Dojazd: {'Tak' if self.travel_var.get() else 'Nie'}"

        tk.Label(self.frame5, text=summary, justify="left").pack()

        tk.Button(self.frame5, text="Zatwierdź", command=self.root.quit).pack()
        self.frame5.pack()

    def clear_frame(self):
        for frame in [self.frame1, self.frame2, self.frame3, self.frame4, self.frame5]:
            frame.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    app = WorkEntryApp(root)
    root.mainloop()
