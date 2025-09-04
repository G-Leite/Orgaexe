import os
from pathlib import Path
from typing import Optional, Literal


class RenomeadorArquivos:
    def __init__(self, pasta: str, prefixo: str, extensao: Optional[str] = None):
        self.pasta = Path(pasta)
        self.prefixo = prefixo
        self.extensao = extensao.lower() if extensao else None

        if not self.pasta.exists():
            raise FileNotFoundError(f"A pasta {self.pasta} não existe.")

    def _listar_arquivos(self) -> list[Path]:
        arquivos = [f for f in self.pasta.iterdir() if f.is_file()]

        if self.extensao:
            arquivos = [f for f in arquivos if f.suffix.lower() == self.extensao]

        return arquivos

    def _ordenar_arquivos(self, arquivos: list[Path], criterio: Literal["nome", "data_criacao", "data_modificacao"]) -> list[Path]:
        #ordem alfabetica
        if criterio == "nome":
            return sorted(arquivos, key=lambda f: f.name.lower())
        #do mais antigo para o mais novo
        elif criterio == "data_criacao":
            return sorted(arquivos, key=lambda f: f.stat().st_ctime)
        #do mais antigo para o mais novo, ou do último alterado para o mais novo
        elif criterio == "data_modificacao":
            return sorted(arquivos, key=lambda f: f.stat().st_mtime)
        else:
            raise ValueError("Critério de ordenação inválido. Use: 'nome', 'data_criacao' ou 'data_modificacao'.")

    def renomear(self, criterio: Literal["nome", "data_criacao", "data_modificacao"] = "nome") -> int:
        arquivos = self._listar_arquivos()
        if not arquivos:
            print("Nenhum arquivo encontrado para renomear.")
            return 0

        arquivos = self._ordenar_arquivos(arquivos, criterio)

        for idx, arquivo in enumerate(arquivos, start=1):
            novo_nome = f"{self.prefixo}-{idx:02d}{arquivo.suffix}"
            novo_caminho = arquivo.with_name(novo_nome)

            os.rename(arquivo, novo_caminho)
            print(f"Renomeado: {arquivo.name} → {novo_nome}")

        print(f"\nTotal renomeado: {len(arquivos)} arquivo(s).")
        return len(arquivos)
