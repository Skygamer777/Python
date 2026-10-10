usuarios = ["Luiz", "Felipe", "Tiago", "Ricardo"]

while True:
    print("\nEscolha uma opção:")
    opcoes = ["Opção 1", "R - Leitura de usuários", "Opção 3", "Opção 4", "Sair"]
    for indice, descricao in enumerate(opcoes, start=1):
        print(f"{indice}. {descricao}")

    try:
        opcao = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    if opcao == 5:
        print("Encerrando o sistema.")
        break
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
    else:
        print("Opção inválida. Tente novamente.")
