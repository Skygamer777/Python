def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def menu():
    print("Escolha uma das opções: ")
    print("1 - Converter Celsius para Fahrenheit")
    print("2 - Converte Fahrenheit para Celsius")
    print("3 - Sair")
opcao = None

while opcao != "3":
    menu()
    opcao = input("Digite sua escolha: ")
    if opcao == "3":
        print("Saindo do programa.")
        break
    if opcao in ['1','2']:
        temperatura = float(input("Digite a temperatura: "))
        
        if opcao == "1": 
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"{temperatura} °C é igual a {resultado} °F")
        elif opcao == '2':
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"{temperatura} °F é igual a {resultado} °C")
        else:
            print("Opção inválida. Tente novamente.")
            
        