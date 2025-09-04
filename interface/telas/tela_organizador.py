import tkinter as tk
from tkinter import filedialog


class TelaOrganizador(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        tk.Label(
            self,
            text="Organizador de Arquivos",
            font=("Arial", 16),
            fg="white",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self,
            text="Selecione uma pasta e organize os arquivos por categoria.",
            font=("Arial", 12),
            fg="white",
            bg="black"
        ).pack(pady=10)

        # === Seleção de pasta ===
        self.caminho_pasta = tk.StringVar(value="Nenhuma pasta selecionada")

        tk.Button(
            self,
            text="Selecionar Pasta",
            command=self.selecionar_pasta,
            fg="white",
            bg="gray20",
            width=20,
            height=2
        ).pack(pady=5)

        tk.Label(
            self,
            textvariable=self.caminho_pasta,
            font=("Arial", 10),
            fg="white",
            bg="black"
        ).pack(pady=5)

        # === Botão Start ===
        tk.Button(
            self,
            text="Start",
            command=self.executar,
            fg="white",
            bg="green",
            width=15,
            height=2
        ).pack(pady=15)

        # === Botão Voltar ===
        tk.Button(
            self,
            text="Voltar",
            command=lambda: controller.mostrar_tela("TelaInicial"),
            fg="white",
            bg="gray20",
            width=15,
            height=2
        ).pack(pady=10)

    def selecionar_pasta(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.caminho_pasta.set(f"Pasta selecionada: {pasta}")

    def executar(self):
        pasta = self.caminho_pasta.get()
        print(f"Start pressionado no Organizador com pasta={pasta}")
