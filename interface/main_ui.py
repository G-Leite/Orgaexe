import tkinter as tk
from interface.telas.tela_inicial import TelaInicial
from interface.telas.tela_renomeador import TelaRenomeador
from interface.telas.tela_organizador import TelaOrganizador
from interface.telas.tela_duplicados import TelaDuplicados


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Organizador de Arquivos")
        self.geometry("600x400")
        self.configure(bg="black")

        container = tk.Frame(self, bg="black")
        container.pack(fill="both", expand=True)

        self.telas = {}
        for Tela in (TelaInicial, TelaRenomeador, TelaOrganizador, TelaDuplicados):
            nome_tela = Tela.__name__
            frame = Tela(parent=container, controller=self)
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("TelaInicial")

    def mostrar_tela(self, nome_tela):
        frame = self.telas[nome_tela]
        frame.tkraise()


def iniciar_interface():
    app = App()
    app.mainloop()
