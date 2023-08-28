# IMPORTAÇÕES
# VARIÁVEIS

valor_p = float(0)
quantidade_p = float(0)
valor_sem_desconto = float(0)
valor_com_desconto = float(0)

# FUNÇÕES
# PROGRAMA PRINCIPAL

print("Bem-Vindo a Loja\n")

while (valor_p <= 0) or (quantidade_p <= 0):      # Validador de valor e quantidade
    valor_p = float(input("Insira o valor do produto: "))
    quantidade_p = float(input("Insira a quantidade deste produto: "))

valor_sem_desconto = (valor_p * quantidade_p)     # Calculando valor sem desconto
print('Valor SEM desconto foi: R$ {:.2f}'.format(valor_sem_desconto))

if (quantidade_p >= 10) and (quantidade_p <= 99):   # Calculando valor com 5% de desconto
    valor_com_desconto = ((valor_sem_desconto) * (0.95))
    print('Valor COM desconto foi: R$ {:.2f} (5% de desconto)'.format(valor_com_desconto))
elif (quantidade_p >= 100) and (quantidade_p <= 999):   # Calculando valor com 10% de desconto
    valor_com_desconto = ((valor_sem_desconto) * (0.90))
    print('Valor COM desconto foi: R$ {:.2f} (10% de desconto)'.format(valor_com_desconto))
elif (quantidade_p>=1000):                               # Calculando valor com 15% de desconto
    valor_com_desconto = ((valor_sem_desconto) * (0.85))
    print('Valor COM desconto foi: R$ {:.2f} (15% de desconto)'.format(valor_com_desconto))
else:                                                   # Sem desconto
    print('Você não ganhou desconto de atacado!')
