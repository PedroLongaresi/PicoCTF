def calcular(expressao):
    try:
        resultado = eval(expressao)
        return resultado
    except:
        return "Expressão inválida"


def numeric(valuepassed):
    verifica = isnumeric(valuepassed)
    if verifica:
        return
    else:
        print("Valor nao numerico")


def main():
    while True:
        print("Digite a operação que deseja realizar (+, -, *, /) ou digite 'sair' para encerrar:")
        operacao = input()
        allowlist = ['+', '-', '*', '/']
        if operacao == "sair":
            break
        if not operacao in allowlist:
            print("Valor Invalido para operador")
            break
        print("Digite o primeiro número:")
        numero1 = input()
        print("Passouaqui")
        retorno = numeric(numero1)
        print("Digite o segundo número:")
        numero2 = input()
        retorno = numeric(numero2)

        expressao = f"{numero1} {operacao} {numero2}"

        resultado = calcular(expressao)
        print(f"O resultado da operação é: {resultado}")


if __name__ == "__main__":
    main()