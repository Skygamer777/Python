while True:
   
    try:
        numero = int(input("Digite um número: "))
        print(f"O dobro de número é: {numero * 2}")
        break
    except ValueError:
        print("Erro: Voce deve digitar um número válido.")