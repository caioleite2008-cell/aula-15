from datetime import datetime

# Entrada
data_nasc_str= input("Digite sua data de nacimento (dd/mm/aaaa):")
data_nascimento = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()

# Ano atual
ano_atual = datetime.today().date().year

# Processamento (apenas diferença de anos)
idade = ano_atual - data_nascimento.year

# Saída
print(f"Sua idade é: {idade} anos")