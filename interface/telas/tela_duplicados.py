import tkinter as tk
from tkinter import filedialog
from core.duplicados import mover_duplicados

class TelaDuplicados(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        tk.Label(
            self,
            text="Remoção de Arquivos Duplicados",
            font=("Arial", 16),
            fg="white",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self,
            text="Selecione uma pasta e mova os arquivos duplicados para 'Duplicados/'.",
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
            command=self.voltar,
            fg="white",
            bg="gray20",
            width=15,
            height=2
        ).pack(pady=10)

        tk.Label(
            self,
            text="Desenvolvido por Guilherme Ferreira Leite",
            font=("Arial", 10),
            fg="white",
            bg="black"
        ).pack(side="bottom", pady=10)

    #método voltar e limpeza do caminho da pasta
    def voltar (self):
        self.caminho_pasta.set("Nenhuma pasta selecionada")
        self.controller.mostrar_tela("TelaInicial")

    #GERENCIADOR DO WINDOWS 
    def selecionar_pasta(self):
        pasta = filedialog.askdirectory()
        if pasta:
            self.caminho_pasta.set(f"Pasta selecionada: {pasta}")

    #CHAMA A PARTE LÓGICA
    def executar(self):
        pasta = self.caminho_pasta.get().replace("Pasta selecionada: ", "")

        if not pasta or pasta.startswith("Nenhuma"):
            tk.messagebox.showerror("Erro", "Selecione uma pasta.")
            return

        try:
            logs = mover_duplicados(pasta)
            if isinstance(logs, list):
                print("\n".join(logs))
                tk.messagebox.showinfo("Sucesso", f"Duplicados movidos. {len(logs)} linhas no log (ver terminal).")
            else:
                tk.messagebox.showinfo("Sucesso", "Operação concluída. Verifique o terminal para detalhes.")
        except Exception as e:
            tk.messagebox.showerror("Erro", str(e))
