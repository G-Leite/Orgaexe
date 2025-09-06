import customtkinter as ctk
from tkinter import filedialog, messagebox
from core.duplicados import mover_duplicados
from __version__ import __version__

class TelaDuplicados(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pasta = None

        # ==== WIDGETS ====
        frame = ctk.CTkFrame(self)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        titulo = ctk.CTkLabel(frame, text="Removedor de Duplicados Semi-Automático", font=("Arial", 22, "bold"))
        titulo.pack(pady=20)

        subtitulo = ctk.CTkLabel(frame, text="Move arquivos duplicados para pasta Duplicados, você decide o que fazer com eles.", font=("Arial", 16))
        subtitulo.pack(pady=20)

        btn_pasta = ctk.CTkButton(frame, text="Selecionar Pasta", command=self.selecionar_pasta, font=("Arial", 16))
        btn_pasta.pack(pady=10)

        btn_executar = ctk.CTkButton(frame, text="Iniciar", command=self.executar, font=("Arial", 16))
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
            mover_duplicados(self.pasta)
            messagebox.showinfo("Sucesso", "Duplicados movidos para a pasta 'Duplicados'!")
            self.pasta = None
        except Exception as e:
            messagebox.showerror("Erro", str(e))
