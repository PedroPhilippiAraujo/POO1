'''
"SOMA SIMPLES"

PARCELA1 = int(input ('digite a primeira parcela: '))
PARCELA2 = int(input ('digite a segunda parcela: '))

Soma = PARCELA1 + PARCELA2

print ('Soma: ', Soma)

'''

'''

"Média 1"

notaA = int(input ('digite a primeira nota: '))
notaB =int(input ('digite a segunda nota: '))

media = (notaA*3.5 + notaB*7.5)/11

print ("média: ", media)

'''

'''
"Média 2"

notaA = int(input ('digite a primeira nota: '))
notaB =int(input ('digite a segunda nota: '))
notaC =int(input ('digite a terceira nota: '))

media = (notaA*2 + notaB*3 + notaC*5)/10

print ("média: ", media)

'''


'''
"Diferenca"

ValorA = int(input('digite o valor A: '))
ValorB = int(input('digite o valor B: '))
ValorC = int(input('digite o valor C: '))
ValorD = int(input('digite o valor D: '))

DIFERENCA = (ValorA * ValorB - ValorC * ValorD)

print ('DIFERENCA = ', DIFERENCA)

'''

'''
"Salario"

numero = int(input('digite o numero do funcionario: '))
horas = int(input('digite o numero de horas trabalhadas: '))
valor = float(input('digite o valor que recebe por hora: '))

salario = horas * valor

print ('NUMBER =',numero)
print ('SALARY = U$',salario)

'''

'''
"Área"

A = float(input('digite o valor A: '))
B = float(input('digite o valor B: '))
C = float(input('digite o valor C: '))


TRIANGULO = (A * C)/2
CIRCULO = 3.14159 * C * C
TRAPEZIO = ((A+B)*C)/2
QUADRADO = B*B
RETANGULO = A*B

print ('TRIANGULO:', TRIANGULO)
print ('CIRCULO:', CIRCULO)
print ('TRAPEZIO:', TRAPEZIO)
print ('QUADRADO:', QUADRADO)
print ('RETANGULO:', RETANGULO)
'''

'''
"Pneu"

N = int(input('digite a pressao desejada: '))
M = int(input('digite a pressao lida pela bomba: '))

dif = N - M

if (N>40) or (N<1) or (M>40) or (M<1):
    print ('ERROR')
else:
        print('DIFERENCA =', dif)
'''

'''
"Busca na Internet"

t = int(input('Quantas pessoas clicaram no terceiro link? '))

link1 = t*4

if (t<1) or (t>1000):
    print ('ERROR')
else:
        print(link1, 'pessoas clicaram no primeiro link')
'''

'''
"Distancia Entre Dois Pontos"

x1 = float(input('X1 = '))
y1 = float(input('Y1 = '))
x2 = float(input('X2 = '))
y2 = float(input('Y2 = '))

dist = ((x2-x1)**2 + (y2-y1)**2)**0.5

print (dist)
'''

'''
"Gasto de Combustivel"

t = int(input('Horas gastas na viagem: '))
v = int(input('Velocidade Média: '))

d = v * t
l = d/12

print (l, 'litros de combustivel')
'''

'''
"Consumo"

x = int(input('Distancia percorrida (Km): '))
y = float(input('Combustivel gasto (l): '))

consumo = x/y

print(consumo, 'Km/l')
'''

'''
"Salario com bonus"

nome = str(input('Nome do Funcionario: '))
salario = int(input('Salario Fixo: '))
venda = float(input('Montante de vendas: '))

total = salario + (venda * 0.15)

print (nome)
print ('TOTAL = R$', total)
'''
