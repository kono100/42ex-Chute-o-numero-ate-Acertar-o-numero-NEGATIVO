
#42. Usando a estrutura de repetição while, elabore um programa que leia números inteiros até
#que seja digitado algum inteiro negativo. Ao final deve apresentar quantos números são pares e quantos são ímpares.

def gera():
    return (1)

def game():
    resposta = -1 or gera()
    tentativa = 0

    chute=0
    while chute is not resposta:
        tentativa +=1

        chute = int(input("Qual seu chute: "))
        if chute <= resposta:
               
            print("\nParabéns Acertou com ",tentativa," tentativas!\n")
        else:
                    print("ERROU")
    
while True:
    game()

#---------------------------- ou 


senha='0'
tentativa =  input("Digite até Acertar: ")

while (senha <= tentativa):

    print("\nTente novamente!\n")
    tentativa=input("Digite até Acertar: ")

print(f"Voce ACERTOU...{tentativa}")