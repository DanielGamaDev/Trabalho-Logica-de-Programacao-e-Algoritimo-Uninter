# IMPORTAÇÕES
# VARIÁVEIS
# FUNÇÕES

def valida_medida(nome_medida):  # Função que valida medidas fornecidas pelo usuário
    while True:
        try:
            # Informa a medida que está sendo pedida ao usuário
            print(("Digite a medida {} do objeto(em cm): ").format(nome_medida), end='')
            medida = int(input())  # Recebe a medida fornecida
            if not medida:  # Se a medida for inválida, retorna ao inicio do laço
                print("Valor inválido! Não pode ser 0! Digite outro valor por favor.")
                continue
            else:
                return medida  # Retorna o valor da medida caso a função seja bem-sucedida
        except:  # Se a medida for inválida(não numérica), retorna ao inicio do laço
            print("Valor inválido! Não numérico! Digite outro valor por favor.")
            continue


def calcula_volume():  # Função dimensoesObjeto, exigência 1
    while True:
        # Recebe as medidas (e as valida na outra função valida_medida)
        comprimento = valida_medida('"comprimento"')
        altura = valida_medida('"altura"')
        largura = valida_medida('"largura"')

        volume = (comprimento * altura * largura)  # Calcula a medida total
        if not volume:  # Se o valor for inválido, para o laço e retorna ao programa principal
            print("Valor inválido! O volume pode ser 0! Digite outros valores por favor.")
            break
        # Verifica cada tamanho e atribui o valor do volume
        if (volume < 1000):
            valor_volume = int(10)
            print("O volume é de {}cm³.".format(volume))
            return valor_volume
        elif (volume >= 1000) and (volume < 10000):
            valor_volume = int(20)
            print("O volume é de {}cm³".format(volume))
            return valor_volume
        elif (volume >= 10000) and (volume < 30000):
            valor_volume = int(30)
            print("O volume é de {}cm³".format(volume))
            return valor_volume
        elif (volume >= 30000) and (volume < 100000):
            valor_volume = int(50)
            print("O volume é de {}cm³".format(volume))
            return valor_volume
        elif (volume >= 100000):  # Caso o volume seja maior que 100000 kg reinicia o laço e exibe o erro ao usuário
            print("O volume é de {}cm³.".format(volume))
            print("Não aceitamos objetos deste tamanho. Por favor digite os valores novamente. \n")
            continue


def valida_peso():  # Função pesoObjeto, exigência 2
    while True:
        try:
            peso = float(input("Digite o peso do objeto(em kg): "))  # Recebe o peso
            if (peso <= 0):  # Valida o peso caso seja igual ou menor que 0
                print("Valor inválido! O peso pode ser 0! Digite outro valor por favor.")
                continue
            else:
                # Cria o multiplicador para cada intervalo de peso
                if (peso <= 0.1):
                    multiplicador_peso = float(1)
                    print("O peso é de {:.3f}kg.".format(peso))
                    # O peso é um float, então decidi deixar o código exibido 3 casas depois da vírgula
                    # Como é usado no dia a dia, lembrando que o "."(ponto) é a nossa ","(vírgula)
                    return multiplicador_peso # Retorna o multiplicador
                elif (peso > 0.1) and (peso < 1):
                    multiplicador_peso = float(1.5)
                    print("O peso é de {:.3f}kg.".format(peso))
                    return multiplicador_peso
                elif (peso >= 1) and (peso < 10):
                    multiplicador_peso = float(2)
                    print("O peso é de {:.3f}kg.".format(peso))
                    return multiplicador_peso
                elif (peso >= 10) and (peso < 30):
                    multiplicador_peso = float(3)
                    print("O peso é de {:.3f}kg.".format(peso))
                    return multiplicador_peso
                # Exibe o erro e reinicia o laço caso peso seja maior que 30
                elif (peso >= 30):
                    print("O peso é de {:.3f}kg.".format(peso))
                    print("Não aceitamos objetos deste peso. Por favor digite o valor novamente. \n")
                    continue
        except: # Retorna ao início do laço caso o valor seja não numérico
            print("Valor inválido! Não numérico! Digite outro valor por favor.")
            continue


def mostra_rota():  # Função que exibe as rotas disponíveis quando chamada
    print("***************** ROTAS DISPONÍVEIS *********************")
    print("| Sigla |   Ponto de partida e Ponto de chegada         |")
    print("#-------------------------------------------------------#")
    print("|  NI  | - De Nova Friburgo-RJ para Itaperuna-RJ        |")
    print("|  NM  | - De Nova Friburgo-RJ para Muriaé-MG           |")
    print("|  IN  | - De Itaperuna-RJ para Nova Friburgo-RJ        |")
    print("|  IM  | - De Itaperuna-RJ para Muriaé-MG               |")
    print("|  MN  | - De Muriaé-MG para Nova Friburgo-RJ           |")
    print("|  MI  | - De Muriaé-MG para Itaperuna-RJ               |")
    print("#-------------------------------------------------------#")
    print("\n")


def escolhe_rota():   # Função rotaObjeto, exigência 3
    while True:
        mostra_rota() # Chama a função que exibe as rotas
        rota_escolhida = str(input("Escolha uma das rotas acima, digite a sigla: ")) # Recebe a rota escolhida
        # Retorna o multiplicador referente a qualquer rota escolhida pelo usuário
        if (rota_escolhida.upper() == 'NI'):
            print("A rota escolhida foi de Nova Friburgo-RJ para Itaperuna-RJ.")
            multiplicador_rota = float(1.2)
            return multiplicador_rota
        elif (rota_escolhida.upper() == 'NM'):
            print("A rota escolhida foi de Nova Friburgo-RJ para Muriaé-MG.")
            multiplicador_rota = float(1.5)
            return multiplicador_rota
        elif (rota_escolhida.upper() == 'IN'):
            print("A rota escolhida foi de Itaperuna-RJ para Nova Friburgo-RJ.")
            multiplicador_rota = float(1.2)
            return multiplicador_rota
        elif (rota_escolhida.upper() == 'IM'):
            print("A rota escolhida foi de Itaperuna-RJ para Muriaé-MG.")
            multiplicador_rota = float(1)
            return multiplicador_rota
        elif (rota_escolhida.upper() == 'MN'):
            print("A rota escolhida foi de Muriaé-MG para Nova Friburgo-RJ.")
            multiplicador_rota = float(1.5)
            return multiplicador_rota
        elif (rota_escolhida.upper() == 'MI'):
            print("A rota escolhida foi de Muriaé-MG para Itaperuna-RJ.")
            multiplicador_rota = float(1)
            return multiplicador_rota
        else: # Caso a rota não exista, reinicia o laço
            print("Esta não é uma resposta válida! Por favor escolha novamente.")
            continue


# PROGRAMA PRINCIPAL

print("Bem-Vindo a Companhia de Logística do aluno Daniel dos Santos Gama, RU: 4121047 \n")
print("-------------------- ETAPA 1 DE 3 --------------------")
valor_volume = calcula_volume()    # Utiliza as funções para calcular o valor do volume
print("-------------------- ETAPA 2 DE 3 --------------------")
multiplicador_peso = valida_peso()  # Utiliza as funções para calcular o multiplicador do peso
print("-------------------- ETAPA 3 DE 3 --------------------")
multiplicador_rota = escolhe_rota()  # Utiliza as funções para calcular o multiplicador da rota

valor_total = (multiplicador_peso * multiplicador_rota * valor_volume) # Calcula o valor total final

print("\n Multiplicador do Peso: {} | Multiplicador da Rota: {} | Valor do Volume: {} |"
.format(multiplicador_peso, multiplicador_rota, valor_volume)) # Exibe os valores calculados anteriormente para o usuário

print("\n O valor total a ser pago por esta entrega é de R${}".format(valor_total)) # Exibe o valor final para o usuário
