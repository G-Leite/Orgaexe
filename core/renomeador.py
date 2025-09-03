import os
from pathlib import Path


def renomear_arquivos(pasta: str, prefixo: str, extensao: str | None = None) -> list[str]:
    """Renomeia arquivos em lote em uma pasta."""
    pasta_path = Path(pasta)
    if not pasta_path.exists() or not pasta_path.is_dir():
        raise FileNotFoundError(f"Pasta não encontrada: {pasta}")

    arquivos = [f for f in pasta_path.iterdir() if f.is_file()]

    if extensao:
        arquivos = [f for f in arquivos if f.suffix.lower() == extensao.lower()]

    if not arquivos:
        raise FileNotFoundError("Nenhum arquivo encontrado para renomear.")

    arquivos.sort()
    logs = []

    for i, arquivo in enumerate(arquivos, start=1):
        nova_extensao = arquivo.suffix if not extensao else extensao
        novo_nome = f"{prefixo}-{i:02d}{nova_extensao}"
        novo_caminho = pasta_path / novo_nome
        arquivo.rename(novo_caminho)
        logs.append(f"Renomeado: {arquivo.name} → {novo_nome}")

    logs.append(f"Total renomeado: {len(arquivos)} arquivo(s).")
    return logs
