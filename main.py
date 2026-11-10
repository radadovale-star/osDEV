import json
import com
from cr import cena1
import jg
from com import p
import os
import quiz
from pathlib import Path
import com as c
BASE_DIR = Path(__file__).resolve().parent
USER_FILE = BASE_DIR / "usuario.json"
def main():
    com.iniciar()
    com.limpar()
    try:
        com.ins()
        p(f"Seja bem-vindo ao osDEV {nome}!\n Para ter uma lista de comandos digite (help)")
        while True:
            exe = input("osdev:~$ ").lower()

            comandos = ["clear", "exit", "help", "echo", "info", "calc", "terminal", "cr", "ppt", "mens", "areac", "area", "per", "quiz", "notas", ""]

            if exe not in comandos:
                print("Opção invalida!")
                continue

            if exe == "clear":
                com.limpar()

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
                com.tempo(0.5)
                print(imp)

            elif exe == "info":
                com.info()
                com.espera()
                com.limpar()

            elif exe == "help":
                com.help()
                

            elif exe == "calc":
                try:
                    nums1 = float(input("Digite seu primeiro numero: "))
                    ops = input("Digite a operação: ")
                    nums2 = float(input("Digite seu segundo numero: "))
                    com.calc(nums1, ops, nums2)
                    com.espera()
                except ZeroDivisionError:
                    print("ERROR: Não é possível dividir por zero!")
                except ValueError:
                    print("ERROR:Não e possivel fazer operações com texto!")
                except Exception as e:
                    print("ERROR: Um problema interno ocorreu: ", e)

            elif exe == "terminal":
                p("Digite sair, pra sair do terminal.")
                while True:
                    terms = input("[TERM]osdev:~$ ").lower()
                    if terms == "sair":
                        break
                    com.term(terms)

            elif exe == "cr":
                cena1()

            elif exe == "ppt":
                jg.ppt()
            elif exe == "mens":
                com.mens()
            elif exe == "area":
                div1 = float(input("Digite o primeiro valor: "))
                div2 = float(input("Digite o segundo valor: "))
                resultado = com.area(div1, div2)
                print(f"O resultado e {resultado}")
            elif exe == "areac":
                div1 = float(input("Digite o primeiro valor: "))
                resultado = com.area_circ(div1)
                print(F"O resultado e {resultado}")
            elif exe == "per":
                div1 = float(input("Digite o primeiro valor: "))
                div2 = float(input("Digite o segundo valor: "))
                resultado = com.perm(div1, div2)
                print(F"O resultado e {resultado}")
            elif exe == "quiz":
                quiz.quiz_1()
                com.tempo(2)
                com.limpar()
            elif exe == "notas":
                c.notas()
                    
    except ValueError:
        print("ERROR: entrada inválida. Confira os valores digitados.")
    except Exception as e:
        print(f"ERROR: ocorreu um problema no software: {e}")


if USER_FILE.exists():
    try:
        with USER_FILE.open("r", encoding="utf-8") as f:
            usuario = json.load(f)
        nome = usuario["nome"]
    except (json.JSONDecodeError, KeyError, OSError) as e:
        print(f"Não foi possível ler {USER_FILE.name}: {e}")
        nome = input("Digite seu nome de usuário: ").strip() or "Usuário"
    main()
else:
    print("Seja-bem vindo ao osdev!")
    com.tempo(2)
    com.limpar()
    print("Vamos instalar o osdev!")
    nome = input("Digite seu nome de usuário: ").strip() or "Usuário"
    usuario = {"nome": nome}
    with USER_FILE.open("w", encoding="utf-8") as f:
        json.dump(usuario, f, indent=4, ensure_ascii=False)
    print(f"Olá, {nome}! Usuário salvo com sucesso.")
    com.tempo(3)
    print("Abrindo osdev...")
    com.tempo(1)
    com.limpar()
    main()


                



