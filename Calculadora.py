print("=== Calculadora Simples Melhorada ===")
print("Digite 'sair' para encerrar, 'c' para limpar tudo e 'b' para apagar último caractere.\n")

historico = []

while True:
    expr = input("Digite a operação: ")

    if expr.lower() == "sair":
        break
    elif expr.lower() == "c":
        expr = ""
        print("Calculadora limpa!")
        continue
    elif expr.lower() == "b":
        if historico:
            # Apaga último caractere do último cálculo
            expr = historico[-1][:-1]
            historico[-1] = expr
            print("Último cálculo atualizado para:", expr)
        else:
            print("Nada para apagar.")
        continue

    try:
        resultado = eval(expr)
        print("Resultado:", resultado)
        # Adiciona ao histórico
        historico.append(expr + " = " + str(resultado))
        # Mostra últimos 5 cálculos
        print("Histórico recente:")
        for h in historico[-5:]:
            print(h)
    except:
        print("Erro! Digite uma operação válida.")