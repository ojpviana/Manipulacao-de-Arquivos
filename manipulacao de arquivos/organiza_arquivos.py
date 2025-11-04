import os
import shutil

pasta = os.getcwd()

tipos = {
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Documentos": [".pdf", ".docx", ".txt", ".html"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Executáveis": [".exe"],
}

arquivos_movidos = 0

for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    # Ignorar o próprio script e pastas
    if arquivo == os.path.basename(__file__) or os.path.isdir(caminho_arquivo):
        continue

    nome, extensao = os.path.splitext(arquivo)
    for tipo, exts in tipos.items():
        if extensao.lower() in exts:
            nova_pasta = os.path.join(pasta, tipo)
            os.makedirs(nova_pasta, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(nova_pasta, arquivo))
            print(f"✅ Movido: {arquivo} → {tipo}")
            arquivos_movidos += 1
            break  # sai do loop interno pra não testar outras categorias

if arquivos_movidos == 0:
    print("⚠️ Nenhum arquivo compatível encontrado para mover.")
else:
    print(f"\n✅ {arquivos_movidos} arquivo(s) organizados com sucesso!")
