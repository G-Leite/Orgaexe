import customtkinter as ctk
from tkinter import filedialog, messagebox
from core.renomeador import renomear_arquivos
from __version__ import __version__

class TelaRenomeador(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pasta = None

         # variável para controlar a escolha única
        self.opcao_var = ctk.IntVar(value=0)

        frame = ctk.CTkFrame(self)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        titulo = ctk.CTkLabel(frame, text="Renomeador de Arquivos", font=("Arial", 22, "bold"))
        titulo.pack(pady=15)

        # seleção de pasta
        btn_pasta = ctk.CTkButton(frame, text="Selecionar Pasta", command=self.selecionar_pasta)
        btn_pasta.pack(pady=5)

        # entrada prefixo
        titulo_prefixo = ctk.CTkLabel(frame, text="Nome para renomeação", font=("Arial", 16, "bold"))
        titulo_prefixo.pack(pady=5)

        self.prefixo_var = ctk.StringVar()
        prefixo_entry = ctk.CTkEntry(frame, textvariable=self.prefixo_var, placeholder_text="Digite o prefixo")
        prefixo_entry.pack(pady=5)

        # entrada extensão
        titulo_extensao = ctk.CTkLabel(frame, text="Extensão Específica", font=("Arial", 16, "bold"))
        titulo_extensao.pack(pady=5)

        self.var_extensao = ctk.StringVar()
        entrada_ext = ctk.CTkEntry(frame, textvariable=self.var_extensao, placeholder_text="Digite extensão (opcional)")
        entrada_ext.pack(pady=5)

        # opções exclusivas (tipo radio button)
        lbl_opcoes = ctk.CTkLabel(frame, text="Escolha uma opção de renomeação:", font=("Arial", 16, "bold"))
        lbl_opcoes.pack(pady=(20, 10))

        rb1 = ctk.CTkRadioButton(frame, text="Renomeia todos os arquivos", variable=self.opcao_var, value=1, font=("Arial", 16))
        rb1.pack(pady=5)
        lbl_rb1 = ctk.CTkLabel(frame, text="Renomeia todos os arquivos encontrados, indepedente da extensão", font=("Arial", 16))
        lbl_rb1.pack(pady=(0, 10))

        linha = ctk.CTkFrame(master=frame, height=2, corner_radius=0, fg_color="gray40")
        linha.pack(fill="x", pady=10, padx=20)

        rb2 = ctk.CTkRadioButton(frame, text="Somente arquivos de extensão específica", variable=self.opcao_var, value=2, font=("Arial", 16))
        rb2.pack(pady=5)
        lbl_rb2 = ctk.CTkLabel(frame, text="Renomeia apenas arquivos com a extensão digitada acima.", font=("Arial", 16))
        lbl_rb2.pack(pady=(0, 10))

        linha = ctk.CTkFrame(master=frame, height=2, corner_radius=0, fg_color="gray40")
        linha.pack(fill="x", pady=10, padx=20)

        rb3 = ctk.CTkRadioButton(frame, text="Renomeia do mais antigo para o mais recente", variable=self.opcao_var, value=3, font=("Arial", 16))
        rb3.pack(pady=5)
        lbl_rb3 = ctk.CTkLabel(frame, text="Renomeia do mais antigo para o mais novo/última vez modificado. O mais antigo será o 01. ", font=("Arial", 16))
        lbl_rb3.pack(pady=(0, 10))

        # botão de execução
        btn_executar = ctk.CTkButton(frame, text="Iniciar", command=self.executar)
        btn_executar.pack(pady=10)

        # botão de voltar
        btn_voltar = ctk.CTkButton(frame, text="Voltar", command=lambda: controller.mostrar_tela("TelaInicial"))
        btn_voltar.pack(pady=10)

        versao = f"Versão {__version__}"
        label_versao = ctk.CTkLabel(frame, text=versao, font=("Arial", 12))
        label_versao.pack(side="bottom", pady=10)

    def selecionar_pasta(self):
        self.pasta = filedialog.askdirectory()
        if self.pasta:
            messagebox.showinfo("Pasta Selecionada", f"Pasta: {self.pasta}")

    def executar(self):
        if not self.pasta:
            messagebox.showerror("Erro", "Escolha uma pasta antes de executar.")
            return

        prefixo = self.prefixo_var.get().strip()
        if not prefixo:
            messagebox.showerror("Erro", "Digite um prefixo.")
            return

        opcao = self.opcao_var.get()
        extensao = self.var_extensao.get().strip() or None

        if opcao == 0:
            messagebox.showerror("Erro", "Escolha uma opção de renomeação.")
            return

        try:
            # Aqui você pode passar a 'opcao' para o core e tratar lá
            renomear_arquivos(self.pasta, prefixo, extensao, opcao)
            messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")
            self.prefixo_var.set("")
            self.var_extensao.set("")
            self.opcao_var.set(0)
            self.pasta = None
        except Exception as e:
            messagebox.showerror("Erro", str(e))
