from datetime import datetime

# Entrada
data_str = input("digite a data de devolução do livro (dd/mm/aaaa)")
data_devolucao = datetime.strptime(data_str, "%d/%m/%Y").date()

# Data atual
hoje = datetime.today().date()

# Processamento
if data_devolucao > hoje:
    dias = (data_devolucao - hoje).days
    print(f"Você tem {dias} dias para devolver.")
elif data_devolucao < hoje:
    dias = (hoje - data_devolucao).days
    print(f"O livro está atrasado em {dias} dias.")
else:
    print("O livro vence hoje.")        