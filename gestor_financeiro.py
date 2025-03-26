# Gestor Financeiro

despesas = []  # Lista para armazenar despesas
receitas = []  # Lista para armazenar receitas

def main():
    print("Bem-vindo ao Gestor Financeiro!")
    # Menu interativo
    while True:
        print("\nEscolha uma opção:")
        print("1. Registrar despesa")
        print("2. Registrar receita")
        print("3. Exibir resumo financeiro")
        print("4. Sair")
        opcao = input("Digite o número da opção: ")
        
        if opcao == '1':
            registrar_despesa()
        elif opcao == '2':
            registrar_receita()
        elif opcao == '3':
            exibir_resumo()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def registrar_despesa():
    valor = float(input("Digite o valor da despesa (sem o prefixo R$): ").strip())
    descricao = input("Digite a descrição da despesa: ")
    despesas.append({'valor': valor, 'descricao': descricao})

def registrar_receita():
    valor = float(input("Digite o valor da receita: "))
    descricao = input("Digite a descrição da receita: ")
    receitas.append({'valor': valor, 'descricao': descricao})

def exibir_resumo():
    global despesas, receitas
    total_despesas = sum(d['valor'] for d in despesas)
    total_receitas = sum(r['valor'] for r in receitas)
    saldo_liquido = total_receitas - total_despesas
    
    print("\nResumo Financeiro:")
    print("Despesas:")
    for despesa in despesas:
        print(f"- {despesa['descricao']}: R${despesa['valor']:.2f}")
    print("Receitas:")
    for receita in receitas:
        print(f"- {receita['descricao']}: R${receita['valor']:.2f}")
    
    print(f"\nSaldo Líquido: R${saldo_liquido:.2f}")


if __name__ == "__main__":
    main()
