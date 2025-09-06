import customtkinter as ctk
from interface.telas.tela_inicial import TelaInicial
from interface.telas.tela_renomeador import TelaRenomeador
from interface.telas.tela_organizador import TelaOrganizador
from interface.telas.tela_duplicados import TelaDuplicados


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Orgaexe - Organizador de Arquivos")
        self.geometry("900x800")  # Janela maior
        self.resizable(True, True)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.telas = {}
        for Tela in (TelaInicial, TelaRenomeador, TelaOrganizador, TelaDuplicados):
            frame = Tela(master=self.container, controller=self)
            self.telas[Tela.__name__] = frame
            frame.pack(fill="both", expand=True)
            frame.pack_forget()

        self.mostrar_tela("TelaInicial")

    def mostrar_tela(self, nome_tela: str):
        for tela in self.telas.values():
            tela.pack_forget()
        self.telas[nome_tela].pack(fill="both", expand=True)


def iniciar_interface():
    app = App()
    app.mainloop()
