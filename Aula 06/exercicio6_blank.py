usuarios = ["Luiz", "Felipe", "Tiago", "Ricardo"]

print("Escolha uma opção:")
opcoes = ["Opção 1","R-Leitura de usuários","Opção 3","Opção 4"]
for i, opcao in enumerate(opcoes, start=1):
    print(f"{i}.{opcao}")
opcao = int(input("Digite o número da opção desejada: "))

while opcao > 0 and opcao < 5: 
    if opcao == 1:
        print("Você escolheu a opção 1.")

    elif opcao == 2:
        print("Você escolheu a opção Leitura.")  
        for usuario in usuarios:
            print(usuario) 

    elif opcao == 3:
        print("Você escolheu a opção 3.")

    elif opcao == 4:
        print("Você escolheu a opção 4.")

    opcao = int(input("Digite o número da opção desejada: "))

print("Opção inválida. Tente novamente.")
print("Encerrando o sistema")




