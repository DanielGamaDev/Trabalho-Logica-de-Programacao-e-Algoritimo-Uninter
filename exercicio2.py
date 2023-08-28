# IMPORTAÇÕES
# VARIÁVEIS
# FUNÇÕES

def mostrar_cardapio():  # Mostra o cardápio quando é chamada
    print("********************* CARDÁPIO **************************")
    print("| Código  |          Descrição               |   Valor  |")
    print("$-------------------------------------------------------$")
    print("|   100   |        Cachorro-Quente            | R$09,00 |")
    print("|   101   |        Cachorro-Quente Duplo      | R$11,00 |")
    print("|   102   |        X-Egg                      | R$12,00 |")
    print("|   103   |        X-Salada                   | R$13,00 |")
    print("|   104   |        X-Bacon                    | R$14,00 |")
    print("|   105   |        X-Tudo                     | R$17,00 |")
    print("|   200   |        Refrigerante Lata          | R$05,00 |")
    print("|   201   |        Chá Gelado                 | R$04,00 |")
    print("$-------------------------------------------------------$")
    print("\n")


def escolher_produto(codigo_p):  # Cria um novo pedido quando é chamada
    global valor_total, pedido_existe  # Declara variáveis como global, para serem usadas na função e no código principal
    x = int(codigo_p)
    if (x == 100):
        print("Você pediu um Cachorro-Quente no valor de R$09,00.")
        valor_total += 9  # Soma o valor do produto pedido no valor total
        pedido_existe = int(1) # Caso o código seja válido, a variável recebe o valor 1, para aprovar o pedido no laço de repetição
    elif (x == 101):
        print("Você pediu um Cachorro-Quente Duplo no valor de R$11,00.")
        valor_total += 11
        pedido_existe = int(1)
    elif (x == 102):
        print("Você pediu um X-Egg no valor de R$12,00.")
        valor_total += 12
        pedido_existe = int(1)
    elif (x == 103):
        print("Você pediu um X-Salada no valor de R$13,00.")
        valor_total += 13
        pedido_existe = int(1)
    elif (x == 104):
        print("Você pediu um X-Bacon no valor de R$14,00.")
        valor_total += 14
        pedido_existe = int(1)
    elif (x == 105):
        print("Você pediu um X-Tudo no valor de R$17,00.")
        valor_total += 17
        pedido_existe = int(1)
    elif (x == 200):
        print("Você pediu um Refrigerante Lata no valor de R$05,00.")
        valor_total += 5
        pedido_existe = int(1)
    elif (x == 201):
        print("Você pediu um Chá Gelado no valor de R$04,00.")
        valor_total += 4
        pedido_existe = int(1)
    else:
        print("Opção Inválida, não existe um produto com este código, por favor insira outro.")
        pedido_existe = int(0) # Faz a variável receber 0 para que o laço se repita


# PROGRAMA PRINCIPAL

print("Bem-Vindo a Lanchonete do aluno Daniel dos Santos Gama, RU: 4121047 \n")
valor_total = float(0)
pedido_existe = int(0)
mostrar_cardapio()        # Chama a função que mostra o Cardápio

while True:               # Cria um laço de repetição infinito, ou até que o usuário o encerre
    codigo_p = input("Insira o código do produto desejado: ") # Recebe o código do pedido
    escolher_produto(codigo_p)  # Envia o código do pedido para a função que vai somar o valor final
    if (pedido_existe == 0):    # Caso o código seja inexistente, reinicia o laço
        continue
    elif (pedido_existe == 1):  # Caso o código seja existente, continua com a outra opção
        continuar_pedido = str(input("Deseja mais alguma coisa? [S/N]"))
        if (continuar_pedido.upper() == 'S'): # Dá continuidade ao laço
            continue
        elif (continuar_pedido.upper() == 'N'): # Encerra o laço
            break
        else:
            print("Vou interpretar isto como um não, finalizando pedido...\n")
            break

print("O valor total a ser pago é de R${:.2f}".format(valor_total)) # Mostra o valor total final
