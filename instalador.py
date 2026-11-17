
import os
import sys
import subprocess
import tempfile
import urllib.request
import zipfile
import venv
import shutil

URL = "https://github.com/radadovale-star/osDEV/raw/refs/heads/main/osdev.zip"

PACOTES = [
    "pandas",
    "numpy",
    "requests"
]


# ==============================
# SISTEMA
# ==============================

def obter_desktop():
    home = os.path.expanduser("~")

    if sys.platform.startswith("linux"):
        try:
            desktop = subprocess.check_output(
                ["xdg-user-dir", "DESKTOP"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip()

            if desktop and os.path.abspath(desktop) != os.path.abspath(home):
                return desktop

        except (FileNotFoundError, subprocess.CalledProcessError):
            pass

    candidatos = [
        os.path.join(home, "Desktop"),
        os.path.join(home, "Área de Trabalho"),
        os.path.join(home, "Área de trabalho"),
        os.path.join(home, "OneDrive", "Desktop")
    ]

    for caminho in candidatos:
        if os.path.isdir(caminho):
            return caminho

    padrao = os.path.join(home, "Desktop")
    os.makedirs(padrao, exist_ok=True)

    return padrao


def baixar(url, destino):
    requisicao = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(requisicao, timeout=60) as resposta:
        with open(destino, "wb") as arquivo:
            while True:
                bloco = resposta.read(65536)

                if not bloco:
                    break

                arquivo.write(bloco)


def extrair_seguro(zip_file, destino):
    destino = os.path.abspath(destino)

    for membro in zip_file.infolist():
        caminho = os.path.abspath(
            os.path.join(destino, membro.filename)
        )

        if os.path.commonpath([destino, caminho]) != destino:
            raise ValueError("O ZIP contém um caminho inválido!")

    zip_file.extractall(destino)


# ==============================
# AMBIENTE VIRTUAL
# ==============================

def criar_ambiente(pasta):
    ambiente = os.path.join(pasta, ".venv")

    print("\n[1/3] Criando ambiente virtual...")

    if os.path.exists(ambiente):
        print("Ambiente virtual já existe.")
    else:
        venv.create(ambiente, with_pip=True)

    if sys.platform == "win32":
        python = os.path.join(
            ambiente, "Scripts", "python.exe"
        )
    else:
        python = os.path.join(
            ambiente, "bin", "python"
        )

    if not os.path.isfile(python):
        raise FileNotFoundError(
            "Não foi possível localizar o Python do ambiente virtual."
        )

    return python


# ==============================
# DEPENDÊNCIAS
# ==============================

def instalar_pacotes(python):
    print("\n[2/3] Instalando dependências...")

    subprocess.check_call([
        python,
        "-m",
        "pip",
        "install",
        "--disable-pip-version-check",
        "--upgrade",
        "pip"
    ])

    subprocess.check_call([
        python,
        "-m",
        "pip",
        "install",
        "--disable-pip-version-check",
        *PACOTES
    ])

    print("\nDependências instaladas com sucesso!")


# ==============================
# INSTALADOR
# ==============================

def main():
    print("=" * 45)
    print("             osDEV INSTALLER")
    print("=" * 45)

    desktop = obter_desktop()
    destino = os.path.join(desktop, "osDEV")

    print(f"\nDestino: {destino}")

    with tempfile.TemporaryDirectory() as temporario:

        arquivo = os.path.join(
            temporario,
            "osdev.zip"
        )

        print("\n[1/3] Baixando osDEV.zip...")

        baixar(URL, arquivo)

        print("\n[2/3] Extraindo arquivos...")

        os.makedirs(destino, exist_ok=True)

        with zipfile.ZipFile(arquivo, "r") as zip_file:
            extrair_seguro(zip_file, destino)

    python = criar_ambiente(destino)

    instalar_pacotes(python)

    print("\n" + "=" * 45)
    print("       INSTALAÇÃO CONCLUÍDA!")
    print("=" * 45)

    print(f"\nPasta: {destino}")
    print(f"Ambiente: {os.path.join(destino, '.venv')}")

    print("\nPara executar o osDEV:")

    if sys.platform == "win32":
        print(r".venv\Scripts\activate")
    else:
        print("source .venv/bin/activate")

    print("\nDepois execute o arquivo principal do osDEV.")


# ==============================
# EXECUÇÃO
# ==============================

if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\n\nInstalação cancelada.")

    except Exception as erro:
        print(f"\nERRO: {erro}")
        sys.exit(1)

    input("\nPressione ENTER para sair...")
