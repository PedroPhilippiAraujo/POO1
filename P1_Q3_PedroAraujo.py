"Pedro Philippi Araujo 21204555"
A = 0
maiorsalario = 0
sexoMS = "X"
idadeMS = 0
idadeMN = 0
nomeMN = "X"
repetir = "S"
def cadastro(A, maiorsalario, sexoMS, idadeMS, idadeMN, nomeMN):
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo(M/F): "))
    while sexo != "M" and sexo != "F":
        sexo = sexo.replace(sexo, input("ERRO! Sexo (M/F): "))
    salario = int(input("Salario: ")) 
    if sexo == "F" and salario < 2000:
        A +=1
    if salario > maiorsalario:
        maiorsalario = salario
        sexoMS = sexoMS.replace(sexoMS, sexo)
        idadeMS = idade
    if idadeMN == 0:
        idadeMN = idade
    if idade <= idadeMN:
        idadeMN = idade
        nomeMN = nomeMN.replace(nomeMN, nome)
    return A, maiorsalario, sexoMS, idadeMS, idadeMN, nomeMN
    

while repetir == "S":
    A, maiorsalario, sexoMS, idadeMS, idadeMN, nomeMN = cadastro(A, maiorsalario, sexoMS, idadeMS, idadeMN, nomeMN ) 
    repetir = repetir.replace("S", input("deseja registrar um novo usuario?(S/N) "))

print("Existem {} mulheres com salario menor que 2000".format(A))        
print("A pessos com maior salario é {} e tem {} anos de idade".format(sexoMS, idadeMS))
print("O morador mais novo se chama {}".format(nomeMN))
        
        
        
        
        