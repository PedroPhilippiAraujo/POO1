"Pedro Philippi Araujo 21204555"

matriz = list()
linha = list()
mvp = 0
final = 0

N, M = input("digite o numero de jogadores e o numero de partidas: ").split()
N = int(N)
M = int(M)


while N < 1 or N > 100:
    N = int("Erro! N deve estar entre 1 e 100, digite outro numero:")
    
while M < 1 or M > 100:
    M = int("Erro! N deve estar entre 1 e 100, digite outro numero:")
    
    
linha = [0] * M
matriz = [linha] * N

for i in range(N):
    linha = []
    for j in range(M):
        numero = int(input("Digite a quantidade de gols que o jogador {} fez na partida {} :".format(i+1, j+1)))
        linha.append(numero)
    matriz[i] = linha

for i in range(N):
    mvp = 1
    for j in range (M):
        if matriz[i][j] == 0:
            mvp = 0
    if mvp == 1:
        final += 1

print(final)
    

