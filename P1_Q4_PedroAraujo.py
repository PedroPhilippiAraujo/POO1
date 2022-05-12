"Pedro Philippi Araujo 21204555"

def jogo(N, M):
    for num in range(2,N+1):
        prime = 1
        for i in range(2,num):
            if (num%i==0):
                prime = 0
        if prime == 1:
            p1 = num
        
    for num in range(2,M+1):
        prime = 1
        for i in range(2,num):
            if (num%i==0):
                prime = 0
        if prime == 1:
            p2 = num

    final = p1 * p2
    print(final)


N, M = str(input("Digite os valores de N e M: ")).split()
N = int(N)
M = int(M)

while N < 2 or M > 1000:
    print("ERRO! N deve ser maior que 2 e M deve ser menor que 1000")
    N, M = str(input("Digite os valores de N e M: ")).split()
    N = int(N)
    M = int(M)

jogo(N, M)
print("Programa Encerrado. Obrigado por Jogar")