"Pedro Philippi Araujo 21204555"

participantes = list()
continuar = ("S")
acerto = 0
X = int(input("Digite o numero de participantes: "))

while X < 3 or X > 20:
    print("Erro! O numero de participantes deve estar entre 3 e 20")
    X = int(input("Digite o numero de participantes: "))


for i in range (0, X): 
    pessoa = dict()
    a, b, c, d = input("Digite o nome e tres sugestões de presentes: ").split()
    pessoa['nome'] = a
    pessoa['presente1'] = b
    pessoa['presente2'] = c
    pessoa['presente3'] = d

    participantes.append(pessoa)

while continuar == "S":
    buscanome, buscaitem = input("Digite o nome e o presente: ").split()
    
    for e in participantes:
        for v in e.values():
            if v == buscanome:
                for f in participantes:
                    for w in e.values():
                        if w == buscaitem:
                            acerto = 1

    if acerto == 1:
        print("Seu amigo secreto vai adorar")
    else:
        print("Tente outro presente!")

    acerto = 0
    continuar = continuar.replace(continuar, input("deseja continuar?(S/N) "))


print("Fim do programa. Obrigado por utilizar.")
                        
                        
