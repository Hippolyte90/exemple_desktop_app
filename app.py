import customtkinter as ctk
from tkinter import filedialog
from model import train_and_predict

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ML Desktop App")
        self.geometry("400x300")

        self.csv_path = None

        self.label = ctk.CTkLabel(self, text="Sélectionner un fichier CSV")
        self.label.pack(pady=10)

        self.btn_csv = ctk.CTkButton(self, text="Charger CSV", command=self.load_csv)
        self.btn_csv.pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Valeur à prédire")
        self.entry.pack(pady=10)

        self.btn_predict = ctk.CTkButton(self, text="Prédire", command=self.predict)
        self.btn_predict.pack(pady=10)

        self.result = ctk.CTkLabel(self, text="")
        self.result.pack(pady=20)

    def load_csv(self):
        self.csv_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.label.configure(text="CSV chargé ✔")

    def predict(self):
        if not self.csv_path:
            self.result.configure(text="Aucun CSV sélectionné")
            return

        value = float(self.entry.get())
        prediction = train_and_predict(self.csv_path, value)
        self.result.configure(text=f"Résultat : {prediction}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
