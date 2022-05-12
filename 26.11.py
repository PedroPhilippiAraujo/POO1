'''
'aumento de salario'
def salario(sal):
    if sal <= 400.00:
        percent = "15%"
        novosal = sal * 1.15
        reajuste = novosal-sal
        print("Novo salario: ",novosal)
        print("Reajuste ganho: ",reajuste)
        print("Em percentual: ", percent)
    elif 400.00 < sal <= 800.00:
        percent = "12%"
        novosal = sal * 1.12
        reajuste = novosal - sal
        print("Novo salario: ",novosal)
        print("Reajuste ganho: ",reajuste)
        print("Em percentual: ", percent)
    elif 800.00 < sal <= 1200.00:
        percent = "10%"
        novosal = sal *1.10
        reajuste = novosal - sal
        print("Novo salario: ",novosal)
        print("Reajuste ganho: ",reajuste)
        print("Em percentual: ", percent)
    elif 1200.00 < sal <= 2000.00:
        percent = "7%"
        novosal = sal *1.07
        reajuste = novosal - sal
        print("Novo salario: ",novosal)
        print("Reajuste ganho: ",reajuste)
        print("Em percentual: ", percent)
    elif sal > 2000.00:
        percent = "4%"
        novosal = sal *1.04
        reajuste = novosal - sal
        print("Novo salario: ",novosal)
        print("Reajuste ganho: ",reajuste)
        print("Em percentual: ", percent)
        

salario(float(input("Digite o salario: ")))

'''
 
'''
"Fuso Horario"

def fuso(saida, viagem, fuso):
    final = saida + viagem + fuso
    if final > 24:
        final = final - 24
    elif final < 0:
        final = final + 24
    print(final)
    
fuso(int(input("digite o horario de saida: ")), int(input("digite o tempo de viagem: ")), int(input("digite o fuso horario: ")))

'''

'''
"Ultrapassando Z"


def funcao(x,z):
    y = 0
    cont = 1
    soma = 0
    while z<=x:
        z = int(input("Z: "))
    
    while x<z:
        cont +=1
        x = x + y
        y = x + 1
    print (cont)

funcao(int(input("X: ")), int(input("Z: ")))
'''

'''
"media de idades"

def idades(idade):
    cont = 0
    soma = 0
    while idade >= 0:
        soma = soma + idade
        idade = int(input("digite a idade: "))
        cont += 1
    
    media = soma / cont
    print(media)
idades(int(input("digite a idade: ")))
'''

'''
"positivos e media"
def funcao():
    cont = 0
    soma = 0
    positivo = 0
    while cont < 6:
        x = float(input("X: "))
        cont += 1
        if x > 0:
            soma = soma + x
            positivo += 1

    media = soma / positivo
    print(media)
    print(positivo)

funcao()
'''
'''
"Quadrante"

def quadrante(x,y):

    while x != 0 and y != 0:
        if x>0 and y>0:
            print ("primeiro")
        elif x<0 and y>0:
            print ("segundo")
        elif x<0 and y<0:
            print ("terceiro")
        elif x>0 and y<0:
            print ("quarto")
        x = int(input("X: "))
        y = int(input("Y: "))
    
quadrante(int(input("X: ")),int(input("Y: ")))
'''
'''
"elevador"
def elev(N,C):
    cont = 0
    atual = 0
    excesso = 0
    while cont < N:
        cont += 1
        S = int(input("digite a quantidade de pessoas que sairam: "))
        E = int(input("digite a quantidade de pessoas que entraram: "))
        atual = atual + E - S
        if atual < 0:
            atual = 0
        if atual > C:
            excesso = 1
    if excesso == 1:
        print ('S')
    else:
        print ('N')
    
elev(int(input("digite o numero de leituras: ")), int(input("digite a capacidade maxima: ")))
'''
'''
"colchao"

def ah():
    A = int(input("Altura do colchao: "))
    B = int(input("Largura do colchao: "))
    C = int(input("Comprimento do colchao: "))
    H = int(input("Altura da porta: "))
    L = int(input("Largura da porta: "))
    if A <= H and B <= L:
        S = 1
    elif B <= H and A <= L:
        S = 1
    elif B <= H and C <= L:
        S = 1
    elif C <= H and B <= L:
        S = 1
    elif C <= H and A <= L:
        S = 1
    elif A <= H and C <= L:
        S = 1
    else:
        S = 0
    return S

Passe = ah()

if Passe == 1:
    print("Parabéns pela compra João!")
else:
    print("Sinto Muito João. É necessario que você procure um colchão menor")
'''
'''
"Media calculo"
def media(Aluno1, Aluno2, Aluno3, Aluno4, Aluno5):
    mediaturma = (Aluno1 + Aluno2 + Aluno3 + Aluno4 + Aluno5)/5
    return mediaturma
def melhor(Aluno1, Aluno2, Aluno3, Aluno4, Aluno5):
    if Aluno1>Aluno2 and Aluno1>Aluno3 and Aluno1>Aluno4 and Aluno1>Aluno5:
        melhornota = 1
    elif Aluno2>Aluno1 and Aluno2>Aluno3 and Aluno2>Aluno4 and Aluno2>Aluno5:
        melhornota = 2
    elif Aluno3>Aluno1 and Aluno3>Aluno2 and Aluno3>Aluno4 and Aluno3>Aluno5:
        melhornota = 3
    elif Aluno4>Aluno1 and Aluno4>Aluno2 and Aluno4>Aluno3 and Aluno4>Aluno5:
        melhornota = 4
    elif Aluno5>Aluno1 and Aluno5>Aluno2 and Aluno5>Aluno3 and Aluno5>Aluno4:
        melhornota = 5
    return melhornota
Aluno1 = int(input("digite a nota do aluno 1: "))
Aluno2 = int(input("digite a nota do aluno 2: "))
Aluno3 = int(input("digite a nota do aluno 3: "))
Aluno4 = int(input("digite a nota do aluno 4: "))
Aluno5 = int(input("digite a nota do aluno 5: "))

med = media(Aluno1, Aluno2, Aluno3, Aluno4, Aluno5)
melhoraluno = melhor(Aluno1, Aluno2, Aluno3, Aluno4, Aluno5)     
print("Média da turma: ",med)
print("Aluno {} foi o melhor aluno".format(melhoraluno))

'''
'''
def funcao(X):
    if (X % 2) == 0:
        Y = "Par"
    else:
        Y = "Impar"
    return Y
cont = 0
while cont < 10:
    cont += 1
    Z = funcao(int(input("Digite um numero: ")))
    print(Z)
'''    
