'''
"ida a feira"
prods = dict()
P = 0
M = 0
total = 0

while P < 1 or P > M:
    M = int(input("digite a quantidade diferentes: "))
    P = int(input("quantas frutas ela vai comprar?: "))
    if P < 1 or P > M:
        print("Erro! Digite novamente")


for i in range(0,P):
    prods[float(input("digite o valor do produto"))] = str(input("Digite o nome da fruta: "))
    
for e in prods.keys():
    total = total + e
    
print(total)

'''
'''
cartas = {}
kids = {}
n = int(input("numero traducoes: "))
m = int(input("quantidade de criancas: "))

    
for i in range (0,n):
    cartas[str(input("digite o nome da lingua: "))] = str(input("digite a mensagem: "))
    

for i in range (0,m):
    kids[str(input("digite o nome da crianca: "))] =  str(input("digite a lingua da crianca: "))
    
    
for e in kids.values():
    for v in cartas.keys():
        if (e == v):
            kids[e] = cartas[v]
                
'''            
            
    
