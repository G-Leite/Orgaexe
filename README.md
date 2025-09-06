# 📂 Orgaexe
## 📌 Estado Atual

✅ Lógica core pronta (renomeador, organizador, duplicados)

✅ Interface em customtkinter funcionando

✅ Testado manualmente, erros corrigidos (paths, botões voltar, etc.)

✅ Check-boxes no Renomeador implementadas e funcionando

✅ Projeto rodando via main.py

⚠️ Ainda não empacotado em .exe

⚠️ Versão ainda não definida no código

⚠️ Interface ainda precisa de ajustes finos (centralização perfeita, responsividade, textos longos, etc.)

💤 Alguns "extras" (mostrar caminho da pasta, reset de paths automáticos, refinamento da UX) ficaram para próxima versão.

## 🚀 Como rodar
Requisitos:
python >= 3.10
pip install -r requirements.txt

Requisitos:
python main.py

## 📦 Como empacotar

Usando PyInstaller:
pip install pyinstaller
pyinstaller --onefile --windowed main.py

O executável sai em:
dist/main.exe

Teste em outra máquina sem Python para confirmar que roda sem dependências.
Anexe o .exe na próxima Release do GitHub.

## 🏷️ Versão

Próxima versão a marcar: v0.1.0

Guardar no código em core/__init__.py:

## Checklist futuro

### Curto prazo 
Criar ícone para o .exe
Mostrar caminho da pasta selecionada.
Mostrar caminho da pasta selecionada.
Melhorar mensagens de erro/popups.

### Médio Prazo
Criar CHANGELOG.md para acompanhar evolução
Adicionar testes unitários básicos
Tela com prévia das mudanças 

### Longo Prazo
Empacotar para Linux/MAC
Melhorar UX 

## Notas Rápidas
Interface → está OK, não mexer agora.

Renomeador → tem check-box com escolha única (ordem mais antiga/mais nova).

Não esquecer: ao empacotar com PyInstaller, testar no Windows limpo.

Onde paramos: preparando para a versão 1.0.0 (primeira release “vendável”).






