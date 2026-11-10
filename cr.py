import os
import time



def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")




def esperar():
    input("\nPressione ENTER para continuar...")


def escolher(opcoes):
    while True:
        escolha = input("\nEscolha: ")

        if escolha in opcoes:
            return escolha

        print("\nEscolha inválida!")


def cena1():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║        A REVOLTA DE ESPÁRTACO        ║
╚══════════════════════════════════════╝

          __________________
         /                  \
        /   ESCOLA DE       \
       /    GLADIADORES      \
      /______________________\
          |  |  |  |
          |  |  |  |
          |__|__|__|

             ROMA, 73 a.C.
""")

    print("Você vive como escravizado em uma escola de gladiadores.")
    print("A vida é difícil, e todos sonham com a liberdade.")
    print()
    print("Espártaco está planejando uma fuga.")
    print()
    print("[1] Juntar-se ao plano de Espártaco.")
    print("[2] Ficar em silêncio e observar.")
    print("[3] Avisar os responsáveis pela escola.")

    escolha = escolher(("1", "2", "3"))

    if escolha == "1":
        cena2()

    elif escolha == "2":
        print("\nVocê decide observar o que está acontecendo...")
        esperar()
        cena2()

    elif escolha == "3":
        print("\nVocê decide não participar da fuga.")
        print("A história de Espártaco continuará sem você.")


        esperar()
        final_derrota()


def cena2():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║               A FUGA                ║
╚══════════════════════════════════════╝

             .-.
            /   \
           /     \
          |       |
          |  []   |
          |       |
      ____|_______|____
           |   |
           |   |

              NOITE
""")

    print("Durante a noite, Espártaco e seus companheiros conseguem escapar.")
    print("Vocês deixam a escola e procuram um lugar seguro.")
    print()
    print("[1] Procurar um lugar seguro.")
    print("[2] Enfrentar os romanos imediatamente.")
    print("[3] Convencer mais escravizados a se juntarem.")

    escolha = escolher(("1", "2", "3"))

    if escolha == "1":
        cena3()

    elif escolha == "2":
        print("\nO grupo ainda não está preparado para um confronto... Mais vocẽ ignora os avisos de seus aliados")
        esperar()
        final_estranho()

    elif escolha == "3":
        cena3()


def cena3():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║              O VESÚVIO               ║
╚══════════════════════════════════════╝

             /\
            /  \
           /    \
          /      \
         /  /\    \
        /  /  \    \
       /__/____\____\

              VESÚVIO
""")

    print("O grupo chega à região do Monte Vesúvio.")
    print("Os romanos tentam cercar os revoltosos.")
    print("Espártaco consegue encontrar uma maneira de escapar.")
    print()
    print("[1] Permanecer com o grupo.")
    print("[2] Tentar deixar a região.")
    print("[3] Ajudar a organizar os novos integrantes.")

    escolha = escolher(("1", "2", "3"))

    cena4()


def cena4():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║          A REVOLTA CRESCE            ║
╚══════════════════════════════════════╝

       O O O O O O
      /|/|/|/|/|/|
       | | | | | |
      / \ / \ / \ / \

          O GRUPO CRESCE
""")

    print("A revolta já não é apenas uma pequena fuga.")
    print("Milhares de pessoas passam a acompanhar Espártaco.")
    print()
    print("[1] Tentar sair da Itália.")
    print("[2] Continuar enfrentando Roma.")
    print("[3] Procurar uma região segura.")

    escolha = escolher(("1", "2", "3"))
    if escolha == "2":
        print("\nO grupo ainda não está completamente completo para um confronto... Mais vocẽ ignora os avisos de seus aliados")
        esperar()
        final_estranho2()
    else:    
        cena5()


def cena5():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║             A DECISÃO                ║
╚══════════════════════════════════════╝

              |
           \  |  /
            \ | /
          --- O ---
            / | \
           /  |  \

           QUAL CAMINHO?
""")

    print("O grupo está dividido sobre o que fazer.")
    print()
    print("[1] Tentar deixar a Itália.")
    print("[2] Continuar com Espártaco.")
    print("[3] Procurar outro grupo de fugitivos.")

    escolha = escolher(("1", "2", "3"))

    cena6()


def cena6():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║        O EXÉRCITO ROMANO             ║
╚══════════════════════════════════════╝

          ______________
         |     ROMA     |
         |______________|

          O O O O O O
         /|/|/|/|/|/|
          | | | | | |
         / \/ \/ \/ \

             ROMANOS
""")

    print("Roma envia um grande exército comandado por")
    print("Marco Licínio Crasso para enfrentar a revolta.")
    print()
    print("A situação ficou cada vez mais difícil.")

    esperar()

    final()


def final():
    limpar_tela()

    print(r"""
╔══════════════════════════════════════╗
║               FIM                    ║
╚══════════════════════════════════════╝

             ☀
        \    |    /
         \   |   /
      ----\  |  /----
          \ | /
           \|/

        LIBERDADE?
""")

    print("A Revolta de Espártaco foi derrotada em 71 a.C.")
    print("A revolta não conseguiu acabar com a escravidão em Roma.")
    print()
    print("Mesmo assim, tornou-se um importante episódio")
    print("da história das resistências de pessoas escravizadas.")
    print()

    print("Obrigado por jogar!")
    esperar()


def final_derrota():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║               FIM                    ║
╚══════════════════════════════════════╝

A fuga não aconteceu para você.

Mas a Revolta de Espártaco continuaria
marcando a história de Roma.

              FIM final -2
""")

    esperar()


def final_estranho():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║               FIM                    ║
╚══════════════════════════════════════╝

Vocês foram enfrentar os romanos... mais não deu certo

Seus aliados foram atacar, vocẽ sente algo Perfurando seu peito
todos seus aliados estão mortos... você cai no chão

              FIM Final -1
""")

    esperar()

def final_estranho2():
    limpar_tela()


    print(r"""
╔══════════════════════════════════════╗
║               FIM                    ║
╚══════════════════════════════════════╝

Vocês foram lutar, Foi uma longa batalha mais mesmo assim...

Seus aliados foram atacar, vocẽ sente algo Perfurando seu peito
todos seus aliados estão mortos... você cai no chão

              FIM Final -3
""")

