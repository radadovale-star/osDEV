import com
from com import seta
def escolher(opcoes, certa):
    while True:
        escolha = input("\nEscolha (A, B, C ou D): ").strip().lower()
        if escolha not in opcoes:
            print("\nEscolha inválida!")
            continue
        return escolha == certa


def quiz_1():
    vav = ["a", "b", "c", "d"]
    pontos = 0
    com.limpar()
    print("🧪 Quiz de Ciências — 6º ano\n")   
    com.tempo(3)
    print("Sejam-bem vindos ao quiz!")
    com.tempo(2)
    com.limpar()
    print("1. Qual é a principal função das raízes de uma planta?\n")
    print("""A)Captar a luz do Sol
B) Absorver água e sais minerais do solo
C) Produzir frutos diretamente
D) Produzir sementes""")
    pontos += 100 if escolher(vav, "b") else 0

    com.limpar()
    print("2. Qual órgão é responsável por bombear o sangue pelo corpo?\n")
    print("""A) Pulmão
B) Estômago
C) Coração
D) Rim""")
    pontos += 100 if escolher(vav, "c") else 0

    com.limpar()
    print("3. Como se chama a passagem da água do estado líquido para o gasoso?\n")
    print("""A) Solidificação
B) Condensação
C) Fusão
D) Vaporização""")
    pontos += 100 if escolher(vav, "d") else 0
    com.limpar()
    print("4. Qual destes materiais conduz bem a eletricidade?\n")
    print("""A) Borracha
B) Plástico
C) Cobre
D) Madeira seca""")
    pontos += 100 if escolher(vav, "c") else 0
    com.limpar()
    print("5. Qual gás as plantas absorvem do ar durante a fotossíntese?\n")
    print("""A) Oxigênio
B) Gás carbônico
C) Hélio
D) Hidrogênio""")
    pontos += 100 if escolher(vav, "b") else 0
    com.limpar()
    print("6. Qual é a camada mais externa da Terra?\n")
    print("""A) Núcleo interno
B) Manto
C) Núcleo externo
D) Crosta terrestre""")
    pontos += 100 if escolher(vav, "d") else 0
    com.limpar()
    print("7. Qual instrumento é utilizado para observar células que não conseguimos enxergar a olho nu?\n")
    print("""A) Termômetro
B) Microscópio
C) Bússola
D) Barômetro""")
    pontos += 100 if escolher(vav, "b") else 0
    com.limpar()
    print(f"Sua pontuação final foi.. {pontos} lembre que o maximo e 700!")
    print("Mostrar alternativas certas? (y/n)")
    bauu = input(seta)
    if bauu == "y":
        print("""
1. B) Absorver água e sais minerais do solo.
2. C) Coração.
3. D) Vaporização.
4. C) Cobre.
5. B) Gás carbônico.
6. D) Crosta terrestre.
7. B) Microscópio.""")
        com.tempo(5)
        input("")
    elif bauu == "n":
        com.limpar()
    else:
        com.limpar()































    


