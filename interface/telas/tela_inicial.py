
import customtkinter as ctk
from __version__ import __version__

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)

        frame = ctk.CTkFrame(self)
        frame.pack(pady=40, padx=60, fill="both", expand=True)

        titulo = ctk.CTkLabel(frame, text="OrgaEXE - Organizador de Arquivos", font=("Arial", 24, "bold"))
        titulo.pack(pady=20)

        subtitulo = ctk.CTkLabel(frame, text="Kit de ferramentas automatizadas para manter seu computador organizado.", font=("Arial", 16))
        subtitulo.pack(pady=10)

        escolha = ctk.CTkLabel(frame, text="Escolha uma das opções abaixo:", font=("Arial", 16))
        escolha.pack(pady=10)

        # ===== RENOMEADOR =====
        subtitulo_renomeador = ctk.CTkLabel(frame, text="Padronize o nome dos arquivos da pasta toda ou apenas determinada extensão.", font=("Arial", 16))
        subtitulo_renomeador.pack(pady=5)

        btn1 = ctk.CTkButton(frame, text="Renomeador", command=lambda: controller.mostrar_tela("TelaRenomeador", ), font=("Arial", 16))
        btn1.pack(pady=10)

        linha = ctk.CTkFrame(master=frame, height=2, corner_radius=0, fg_color="gray40")
        linha.pack(fill="x", pady=10, padx=20)

        # ===== ORGANIZADOR =====
        subtitulo_organizador = ctk.CTkLabel(frame, text="Organize seus arquivos dentro de pastas específicas", font=("Arial", 16))
        subtitulo_organizador.pack(pady=5)

        btn2 = ctk.CTkButton(frame, text="Organizador", command=lambda: controller.mostrar_tela("TelaOrganizador"), font=("Arial", 16))
        btn2.pack(pady=10)

        linha = ctk.CTkFrame(master=frame, height=2, corner_radius=0, fg_color="gray40")
        linha.pack(fill="x", pady=10, padx=20)

        # ===== DUPLICADOS =====
        subtitulo_duplicados = ctk.CTkLabel(frame, text="Remova duplicados sem precisar checar um por um", font=("Arial", 16))
        subtitulo_duplicados.pack(pady=5)

        btn3 = ctk.CTkButton(frame, text="Duplicados", command=lambda: controller.mostrar_tela("TelaDuplicados"), font=("Arial", 16))
        btn3.pack(pady=10)

        rodape = ctk.CTkLabel(frame, text="Desenvolvido por Guilherme F. Leite", font=("Arial", 12))
        rodape.pack(side="bottom", pady=10)

        versao = f"Versão {__version__}"
        label_versao = ctk.CTkLabel(frame, text=versao, font=("Arial", 12))
        label_versao.pack(side="bottom", pady=10)
