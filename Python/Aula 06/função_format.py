numeros = [0] *  5

for i in range(5):
    numeros[i] = int(input("Digite o {}º número inteiro: ".format(i + 1)))

for i,numero in enumerate(numeros):
    print("O numero {} está na posição {} da lista.".format(numero,i))