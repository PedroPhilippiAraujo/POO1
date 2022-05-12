"Pedro Philippi Araujo 21204555"

fita = list()
fim = 0
dias = 0

F = int(input("Qual o comprimento da fita? "))

while F < 1 or F > 100:
    print("Erro! Digite um numero entro 1 e 100")
    F = int(input("qual o comprimento da fita? "))

for i in range (0, F+1):
    fita.append(0)

R = int(input("Quantas gotas serão colocadas? "))

while R < 1 or F < R:
    print("Erro! Digite um numero maior que 1 e menor que o comprimento da fita")
    R = int(input("Quantas gotas serão colocadas?"))
    
print("digite quais posições as gotas serão colocadas:")    
for i in range(0, R):
    x = int(input()) - 1
    fita[x] = 1
    
while fim == 0:    
    for i in range (0, F):
        if fita[i] == 1 and fita[i-1] == 0:
            fita[i-1] = 2
        if fita[i] == 1 and fita[i+1] == 0:
            fita[i+1] = 2
        
    for j in range (0, F):
        if fita[j] == 2:
            fita[j] = 1
    dias += 1
    fim = 1
    for g in range (0,F):
        if fita[g] == 0:
            fim = 0

print(dias)
