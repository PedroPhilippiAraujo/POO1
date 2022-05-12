"Pedro Philippi Araujo 21204555"

repetir = "S"
while repetir == "S":
    A, B, C = str(input("Digite os valores de Alice, Beto e Clara: ")).split()
    A = int(A)
    B = int(B)
    C = int(C)

    while A < 0 or A > 1 or B < 0 or B > 1 or C < 0 or C > 1:
        print("ERRO! Use apenas Valores de 0 ou 1")
        A, B, C = str(input("Digite os valores de Alice, Beto e Clara: ")).split()
        A = int(A)
        B = int(B)
        C = int(C)

    if A == 0 and B == 0 and C == 0:
        print("*")
    elif A == 1 and B == 1 and C == 1:
        print("*")
    elif A == 0 and B == 0 and C == 1:
        print("C")
    elif A == 0 and B == 1 and C == 0:
        print("B")
    elif A == 0 and B == 1 and C == 1:
        print("A")
    elif A == 1 and B == 0 and C == 0:
        print("A")
    elif A == 1 and B == 0 and C == 1:
        print("B")
    elif A == 1 and B == 1 and C == 0:
        print("C")

    repetir = repetir.replace("S", input("deseja continuar jogando?(S/N) "))

print("Obrigado por Jogar")