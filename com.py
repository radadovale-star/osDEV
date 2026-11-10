# Sistema osDEV 
import json
import random
import os
import time
from pathlib import Path
arquivo = "usuario.json"
seta = "osdev:~$ "
setaW = "READ-osdev:~$ "
barra = "=========================================================================================================="
def espera():
    print("\nAperte ENTER para continuar...")
    input()

def p(texto):
    print(texto)

def term(terminals):
    os.system(terminals)

def calc(num1, op, num2):
    while True:
        if op == "/":
            print(f"O Resultado foi.. {num1 / num2}")
            break
        elif op == "*":
            print(f"O Resultado foi.. {num1 * num2}")
            break
        elif op == "-":
            print(f"O Resultado foi.. {num1 - num2}")
            break
        elif op == "+":
            print(f"O Resultado foi.. {num1 + num2}")
            break
        else:
            print("Opção invalida.")

def tempo(segs):
    time.sleep(segs)

def ins():
    print(r"""     
================================
           osDEV
================================
""")

def limpar():
    term("cls" if os.name == "nt" else "clear")


def help():
    print(r"""
    echo ~> Mostra um texto(str) na tela
    clear ~> Limpa a tela
    exit ~> Sai do sistema :(
    help ~> Mostra os comandos que você pode usar
    info ~> Informaçoes do OS
    calc ~> Calculadora
    terminal ~> use o terminal do seu pc dentro de osDEV [Cuidado!]
    ppt ~> pedra,papel tesoura
    cr ~> Jogue As Correntes de Roma, via osDEV
    per ~> Calcule o perimetro
    area ~> Calcula a área de um retângulo
    areac ~> Calcula a area de um circulo
    per ~> Calcula o perímetro de um retângulo
    quiz ~> Quiz de Ciências!
    mens ~> Mostra a Mensagem incial
    notas ~> Um sitema de notas no osdev
    """)

def info():
    ins()
    print(r"""
    Sistema Criado por: Rada
    Criado em 12/10/26
    Versão: osDEV Sequoia Pro (v3.7 Beta)

    i use osDEV btw
    """)

def mens():
    ins()

def area(valor1, valor2):
    return valor1 * valor2

def perm(valor1, valor2):
    return 2 * (valor1 + valor2)

def area_circ(raio):
    from math import pi

    area = pi * raio ** 2

    return area








def iniciar():
    # A tela de abertura é opcional; o programa continua sem Pillow/Tk.
    try:
        import tkinter as tk
        from tkinter import Image, ImageTk

        splash = tk.Tk()
        splash.overrideredirect(True)
        splash.configure(bg="black")
        imagem = Image.open(Path(__file__).resolve().parent / "OSD.jpg").convert("RGBA")
        foto = ImageTk.PhotoImage(imagem)
        largura, altura = imagem.size
        tela_largura = splash.winfo_screenwidth()
        tela_altura = splash.winfo_screenheight()
        x = (tela_largura - largura) // 2
        y = (tela_altura - altura) // 2
        splash.geometry(f"{largura}x{altura}+{x}+{y}")
        label = tk.Label(splash, image=foto, bd=0)
        label.pack()
        splash.after(2500, splash.destroy)
        splash.mainloop()
    except Exception as e:
        print(f"Tela de abertura indisponível: {e}")


def ler(arquivo):
    with open(arquivo, "r") as arquivo2:
        dentro = arquivo2.read()
        print(arquivo2)

def escrever(arquivo, escrito):
    with open(arquivo, 'w') as arquivo2:
        escrever = arquivo2.write(escrito)


def notas():
    print("Seja bem-vindo ao sitema de notas!")
    tempo(3)
    limpar()
    while True:
        print("[1] Gravar [2] Ler [3] Sair")
        print(barra)
        print("\n")
        se = input(seta)
        if se == "1":
            limpar()
            
            nome_arquivo = input("Qual vai ser o nome do arquivo?: ").lower()
            print("Criando arquivo...")
            tempo(3)
            print("[Você esta escrevendo no arquivos!] use [Exit] para sair!")
            print(barra)
            p("\n")
            with open(nome_arquivo, 'w') as arquivo:
                while True:

                    linhaw = input(setaW)

                    if linhaw.lower() == "exit":
                        break

                    arquivo.write(linhaw + "\n")
            print("Texto salvo!")
            limpar()
            break

        elif se == "2":
            limpar()
            abir = input("Digite o nome do arquivo: ").lower()
            limpar()
            with open(abir, "r") as arquivo:
                conteudo = arquivo.read()
                print(barra)
                p("\n")
                print(conteudo)
                p("\n")
                print(barra)
                time.sleep(5)

            break
        elif se == "3":
            print("Saindo...")
            tempo(3)
            limpar()
            ins()
            break

       

