import os
import random
import msvcrt
from time import sleep


VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
ROXO = "\033[35m"
CIANO = "\033[36m"
RESET = "\033[0m"


def gerar_matriz(n=10, m=10, min_val=1, max_val=10):
    return [
        [random.randint(min_val, max_val) for _ in range(m)]
        for _ in range(n)
    ]


def laplace(matriz):
    n = len(matriz)

    if n == 1:
        return matriz[0][0]

    if n == 2:
        return (
            matriz[0][0] * matriz[1][1]
            - matriz[0][1] * matriz[1][0]
        )

    determinante = 0

    for coluna in range(n):
        menor = [
            [matriz[i][j] for j in range(n) if j != coluna]
            for i in range(1, n)
        ]

        cofator = ((-1) ** coluna) * matriz[0][coluna]
        determinante += cofator * laplace(menor)

    return determinante


def main():
    print(AMARELO, end="")

    opcao = input(
        "Deseja gerar uma matriz aleatória? (s/n): "
    )

    palavras = ["valor mínimo", "valor máximo"]

    if opcao.lower() == "s":
        n = int(input("Digite o número de linhas da matriz: "))
        m = int(input("Digite o número de colunas da matriz: "))

        valores = []

        for i in range(2):
            valores.append(
                int(input(f"Digite o {palavras[i]}: "))
            )

        matriz = gerar_matriz(
            n,
            m,
            valores[0],
            valores[1]
        )

    else:
        n = int(input("Digite o número de linhas da matriz: "))
        m = int(input("Digite o número de colunas da matriz: "))

        matriz = []

        for i in range(n):
            linha = []

            for j in range(m):
                valor = int(
                    input(
                        f"Digite o valor para a posição "
                        f"({i + 1}, {j + 1}): "
                    )
                )

                linha.append(valor)

            matriz.append(linha)

    print(VERDE, end="")
    print("\nMatriz utilizada:")

    for linha in matriz:
        print(" ".join(f"{valor:3}" for valor in linha))

    print("\nDeterminante da matriz:", laplace(matriz))


def inicio():
    os.system("cls")

    print(AZUL, end="")
    print("+-------------------------------------------------------------------------------+")
    print(
        "                     CALCULADORA DE DETERMINANTE"
    )
    print("+-------------------------------------------------------------------------------+")
    print(RESET, end="")

    sleep(2)


def fim_faculdade():
    os.system("cls")

    while not (msvcrt.kbhit() and msvcrt.getch() == b"\x1b"):
        print(CIANO, end="")
        os.system("cls")

        print("+-------------------------------------------------------------------------------+")
        print(
            "                     Programa finalizado."
        )
        print("+-------------------------------------------------------------------------------+")

        sleep(5)

        os.system("cls")

        print(VERMELHO, end="")
        print("+-------------------------------------------------------------------------------+")
        print(
            "                         Pressione ESC para fechar."
        )
        print("+-------------------------------------------------------------------------------+")

        sleep(2.5)


inicio()

while True:
    main()

    print(ROXO, end="")

    if input("\nDeseja sair? (s/n): ").lower() == "s":
        break

fim_faculdade()