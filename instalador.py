import os
import sys
import subprocess
import tempfile
import urllib.request
import zipfile

URL = "https://github.com/radadovale-star/osDEV/raw/refs/heads/main/osdev.zip"


def obter_desktop():
    """Descobre a pasta da Área de Trabalho no Windows, Linux ou macOS."""
    home = os.path.expanduser("~")

    # Linux: respeita o idioma do sistema (ex: "Área de Trabalho")
    if sys.platform.startswith("linux"):
        try:
            saida = subprocess.check_output(
                ["xdg-user-dir", "DESKTOP"],
                stderr=subprocess.DEVNULL,
                text=True,
            ).strip()
            if saida and os.path.abspath(saida) != os.path.abspath(home):
                return saida
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass

    # Candidatos comuns em qualquer sistema
    candidatos = [
        os.path.join(home, "Desktop"),
        os.path.join(home, "Área de Trabalho"),
        os.path.join(home, "Área de trabalho"),
        os.path.join(home, "OneDrive", "Desktop"),
    ]
    for caminho in candidatos:
        if os.path.isdir(caminho):
            return caminho

    # Se nada existir, cria a pasta padrão
    padrao = os.path.join(home, "Desktop")
    os.makedirs(padrao, exist_ok=True)
    return padrao


def baixar(url, destino):
    # Usa só a biblioteca padrão: não precisa de pip (evita o erro
    # "externally-managed-environment" em Ubuntu, Arch, etc.)
    requisicao = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(requisicao, timeout=60) as resposta, open(destino, "wb") as f:
        while True:
            bloco = resposta.read(1024 * 64)
            if not bloco:
                break
            f.write(bloco)


def main():
    desktop = obter_desktop()
    print(f"Destino: {desktop}")

    # ZIP temporário, apagado automaticamente no final
    with tempfile.TemporaryDirectory() as pasta_temp:
        arquivo = os.path.join(pasta_temp, "osdev.zip")

        print("Baixando osdev.zip...")
        baixar(URL, arquivo)

        print("Extraindo arquivos...")
        with zipfile.ZipFile(arquivo, "r") as zip_file:
            zip_file.extractall(desktop)

    print("Extração concluída!")
    print("Instalação concluída!")


if __name__ == "__main__":
    try:
        main()
    except Exception as erro:
        print(f"Erro durante a instalação: {erro}")
        sys.exit(1)