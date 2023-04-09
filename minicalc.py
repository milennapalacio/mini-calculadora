from time import sleep

print(40*"=")
print("Boas vindas ao primeiro projeto")
print(40*"=")

nome = input("Insira seu nome: ")
print("Iniciando calculadora...")
sleep(3)

print(f"Calculadora iniciada! E aí {nome}, vamos começar?")

continua = "s"
while (continua == "s"):
    num1 = float(input("Digite o primeiro número: "))
    op = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if (op == "+"):
        resultado = num1 + num2
    elif (op == "-"):
        resultado = num1 - num2
    elif (op == "*"):
        resultado = num1 * num2
    elif (op == "/"):
        resultado = num1 / num2
    else:
        resultado = 0

    print(f"O resultado é: {resultado}")

    continua = input("Você deseja continuar? (s/n): ")

print("Fim do programa, até logo!")
