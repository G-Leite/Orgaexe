import customtkinter as ctk
from tkinter import filedialog, messagebox
from core.organizador import organizar_arquivos
from __version__ import __version__

class TelaOrganizador(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pasta = None

        # ==== WIDGETS ====
        frame = ctk.CTkFrame(self)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        titulo = ctk.CTkLabel(frame, text="Organizador de Arquivos", font=("Arial", 22, "bold"))
        titulo.pack(pady=20)

        subtitulo = ctk.CTkLabel(frame, text="Organiza os arquivos em pastas específicas. Exemplo: planilha.xlsx vai para a pasta 'Planilhas', imagem.png vai para a pasta 'Imagens'. ",wraplength=600, font=("Arial", 16))
        subtitulo.pack(pady=20)

        btn_pasta = ctk.CTkButton(frame, text="Selecionar Pasta", command=self.selecionar_pasta, font=("Arial", 16))
        btn_pasta.pack(pady=10)

        btn_executar = ctk.CTkButton(frame, text="Iniciar", command=self.executar)
        btn_executar.pack(pady=20)

        btn_voltar = ctk.CTkButton(frame, text="Voltar", command=lambda: controller.mostrar_tela("TelaInicial"))
        btn_voltar.pack(pady=10)

        rodape = ctk.CTkLabel(frame, text="Desenvolvido por Guilherme F. Leite", font=("Arial", 12))
        rodape.pack(side="bottom", pady=10)

        versao = f"Versão {__version__}"
        label_versao = ctk.CTkLabel(frame, text=versao, font=("Arial", 12))
        label_versao.pack(side="bottom", pady=10)

    # ==== MÉTODOS ====
    def selecionar_pasta(self):
        self.pasta = filedialog.askdirectory()
        if self.pasta:
            messagebox.showinfo("Pasta Selecionada", f"Pasta: {self.pasta}")

    def executar(self):
        if not self.pasta:
            messagebox.showerror("Erro", "Escolha uma pasta antes de executar.")
            return
        try:
            organizar_arquivos(self.pasta)
            messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")
            self.pasta = None
        except Exception as e:
            messagebox.showerror("Erro", str(e))
