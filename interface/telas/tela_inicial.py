import tkinter as tk


class TelaInicial(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        tk.Label(
            self,
            text="Organizador de Arquivos",
            font=("Arial", 20),
            fg="white",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self,
            text="Ferramenta para renomear, organizar e remover duplicados.",
            font=("Arial", 12),
            fg="white",
            bg="black"
        ).pack(pady=10)

        tk.Button(
            self, text="Renomeador", command=lambda: controller.mostrar_tela("TelaRenomeador"),
            fg="white", bg="gray20", width=20, height=2
        ).pack(pady=5)

        tk.Button(
            self, text="Organizador", command=lambda: controller.mostrar_tela("TelaOrganizador"),
            fg="white", bg="gray20", width=20, height=2
        ).pack(pady=5)

        tk.Button(
            self, text="Duplicados", command=lambda: controller.mostrar_tela("TelaDuplicados"),
            fg="white", bg="gray20", width=20, height=2
        ).pack(pady=5)

        tk.Label(
            self,
            text="Desenvolvido por Seu Nome",
            font=("Arial", 10),
            fg="white",
            bg="black"
        ).pack(side="bottom", pady=10)
