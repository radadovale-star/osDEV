import random
from comandos import espera,limpar,ins
def ppt():
    limpar()
    while True:
        print("Escolha pedra, papel ou tesoura!")
        jg = input("osdev:~$ ").lower()

        pptes = ["pedra", "papel", "tesoura"]

        if jg not in pptes:
            print("Opção errada!")
            continue

        pc = random.choice(pptes)

        if (jg == "pedra" and pc == "tesoura") or (jg == "papel" and pc == "pedra") or (jg == "tesoura" and pc == "papel"):
            print("Você ganhou!")
            espera()
            limpar()
            ins()
            break
        elif jg == pc:
            print("Empate")
            espera()
            limpar()
        else:
            print("Você perdeu!")
            espera()
            limpar()
            
        
    