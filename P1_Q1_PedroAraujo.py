"Pedro Philippi Araujo 21204555"

A = int(input("Digite o numero de alunos: "))
while A <= 0 or A > 1000:
    print("ERRO: digite um numero entre 1 e 1000")
    A = int(input("Digite o numero de alunos: "))

C = int(input("Digite o numero de computadores: "))
while C < A or C > 1000:
    print("ERRO: Tente Novamente")
    C = int(input("Digite o numero de computadores: "))
    
X = int(input("Quantos computadores o Caio queimou? "))
while X > C or X > 100:
    print("ERRO: Tente Novamente")
    X = int(input("Quantos computadores o Caio queimou? "))

Y = int(input("Quantos computadores nao possuem compilador? "))
while Y > C or Y > 1000:
    print("ERRO: Tente Novamente")
    Y = int(input("Quantos computadores nao possuem compilador? "))

if (C - X - Y - 1) >= A:
    print("Igor Feliz!")
elif (C - X - Y - 1) < A and (Y / 2) < X:
    print("Caio, a culpa eh sua!")
else:
    print("Igor Bolado!") 