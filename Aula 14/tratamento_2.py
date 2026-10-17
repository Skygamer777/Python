class ErroPersonalizado(Exception):
    def __init__(self, mensagem="Erro personalizado: Valor negativo não permitido."):
        super().__init__(mensagem)

while True: 
    try:
        numero = int(input("Digite um número positivo: "))
        if numero < 0:
            raise ErroPersonalizado
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
        break
    except ValueError:
        print("Erro: Você deve digitar um número válido.")

    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

    except Exception as e:
        print(e)