import random
import time
import os
from comandos import tempo,term,info,help,calc,espera,p,ins,limpar,mens
from Mude_seu_nome_aqui import user
from Jg1 import cena1
from jogos import ppt

ins()
p(f"Seja bem-vindo ao osDEV {user}!\n Para ter uma lista de comandos digite (help)")
while True:
    exe = input("osdev:~$ ").lower()

    comandos = ["clear", "exit", "help", "echo", "info", "calc", "terminal", "cr", "ppt", "mens", ""]

    if exe not in comandos:
        print("Opção invalida!")
        continue

    if exe == "clear":
        limpar()

    elif exe == "exit":
        p("Tem certeza? (Y/n)")
        sair = input("").lower()
        if sair == "n":
            continue
        elif sair == "y":
            exit()
        else:
            exit()

    elif exe == "echo":
        imp = input("[ECHO] osdev:~$ ")
        tempo(0.5)
        print(imp)

    elif exe == "info":
        info()
        espera()
        limpar()

    elif exe == "help":
        help()
        

    elif exe == "calc":
        nums1 = float(input("Digite seu primeiro numero: "))
        ops = input("Digite a operação: ")
        nums2 = float(input("Digite seu segundo numero: "))
        calc(nums1, ops, nums2)
        espera()

    elif exe == "terminal":
        p("Digite sair, pra sair do terminal.")
        while True:
            terms = input("[TERM]osdev:~$ ").lower()
            if terms == "sair":
                break
            term(terms)

    elif exe == "cr":
        cena1()

    elif exe == "ppt":
        ppt()
    elif exe == "mens":
        mens()
    



        



