import tkinter as tk
from tkinter import filedialog
from core.renomeador import RenomeadorArquivos


class TelaRenomeador(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="black")
        self.controller = controller

        tk.Label(
            self,
            text="Renomeador de Arquivos",
            font=("Arial", 16),
            fg="white",
            bg="black"
        ).pack(pady=20)

        tk.Label(
            self,
            text="Aqui você poderá renomear arquivos em lote.",
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

        # === Campo de prefixo ===
        tk.Label(
            self,
            text="Prefixo para os arquivos:",
            font=("Arial", 12),
            fg="white",
            bg="black"
        ).pack(pady=5)

        self.prefixo_var = tk.StringVar()
        tk.Entry(
            self,
            textvariable=self.prefixo_var,
            width=30,
            bg="gray20",
            fg="white",
            insertbackground="white"
        ).pack(pady=5)

        # === Opções de renomeação ===
        self.opcao_var1 = tk.BooleanVar()
        self.opcao_var2 = tk.BooleanVar()
        self.opcao_var3 = tk.BooleanVar()

        tk.Checkbutton(
            self,
            text="Renomear todos os arquivos (mantendo extensão)",
            variable=self.opcao_var1,
            fg="white", bg="black", selectcolor="gray20",
            activebackground="black", activeforeground="white"
        ).pack(anchor="w", padx=50, pady=2)

        tk.Checkbutton(
            self,
            text="Renomear apenas arquivos de extensões específicas",
            variable=self.opcao_var2,
            fg="white", bg="black", selectcolor="gray20",
            activebackground="black", activeforeground="white"
        ).pack(anchor="w", padx=50, pady=2)

        tk.Checkbutton(
            self,
            text="Ordenar do mais antigo para o mais recente",
            variable=self.opcao_var3,
            fg="white", bg="black", selectcolor="gray20",
            activebackground="black", activeforeground="white"
        ).pack(anchor="w", padx=50, pady=2)

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

    #RODA A PARTE LÓGICA
    def executar(self):
        pasta = self.caminho_pasta.get().replace("Pasta selecionada: ", "")
        prefixo = self.prefixo_var.get().strip()


        if not pasta or pasta.startswith("Nenhuma"):
            tk.messagebox.showerror("Erro", "Selecione uma pasta.")
            return
        if not prefixo:
            tk.messagebox.showerror("Erro", "Digite um prefixo para os arquivos.")
            return

        # Definindo opções
        manter_extensao = self.opcao_var.get() == "manter"
        apenas_extensoes = self.opcao_var.get() == "extensoes"

        try:
            RenomeadorArquivos(
                pasta,
                prefixo,
                manter_extensao=manter_extensao,
                apenas_extensoes=apenas_extensoes
            )
            tk.messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")
        except Exception as e:
            tk.messagebox.showerror("Erro", str(e))

