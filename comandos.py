# Sistema osDEV V:TRUE
import random
import os
import time
from Mude_seu_nome_aqui import user
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
    mens ~> Mostra a Mensagem incial
    """)

def info():
    ins()
    print(r"""
    Sistema Criado por: Rada
    Criado em 12/10/26 (Dia das crianças!)
    Versão: osDEV Sequoia (v: 1.05 BETA)

    i use osDEV btw
    """)

def mens():
    ins()
    p(f"Seja bem-vindo ao osDEV {user}!\n Para ter uma lista de comandos digite (help)")































