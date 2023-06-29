# VARIÁVEIS
# FUNÇÕES

def valida_opcao(opcao_escolhida): # Função feita para validar a opção escolhida pelo usuário
    global codigo_peca     # Declaração de variável global, que serve para dar o código às peças e contá-las
    if (opcao_escolhida == 1):
        codigo_peca += 1
        cadastra_peca(codigo_peca)
    elif (opcao_escolhida == 2):
        consulta_peca()
    elif (opcao_escolhida == 3):
        exclui_peca()
    elif (opcao_escolhida == 4):
        mostra_opcoes()
    elif (opcao_escolhida == 0):   # Descarta o número 0 como opção
        print("O número 0 não é uma opção válida, por favor digite outro número.")
    else:   # Alerta o usuário para que escolha uma opção válida
        print("Não entendi a opção desejada, por favor digite um dígito válido.")


def mostra_opcoes():  # Função que mostra a tabela de opções para o usuário
    print("\n")
    print("************** OPÇÕES DISPONÍVEIS **************")
    print("#----------------------------------------------#")
    print("|      DIGITE O NÚMERO DA OPÇÃO DESEJADA       |")
    print("#----------------------------------------------#")
    print("| 1 |          CADASTRAR UMA PEÇA              |")
    print("| 2 |          CONSULTA DE PEÇAS               |")
    print("| 3 |           DELETAR UMA PEÇA               |")
    print("| 4 |       MOSTRAR TABELA DE OPÇÕES           |")
    print("| 5 |          ENCERRAR PROGRAMA               |")
    print("#----------------------------------------------#")
    print("\n")


def cadastra_peca(cod):  # Função cadastrarPeca, exigência 1
    global lista_peca  # Declarando lista_peca para criar as peças
    while True:
        print("--- MENU DE CADASTRO DE PEÇA ---")
        try:
            print("O código do produto é {}".format(cod)) # Apresentando o código do produto ao usuário
            nome = str(input("Digite o NOME da peça: ")) # Pedindo dados da peça ao usuário
            fabricante = str(input("Digite o FABRICANTE da peça: "))
            valor = float(input("Digite o VALOR da peça(em reais): "))
            dicionario_pecas = {'codigo': cod,           # Armazenando dados pedidos ao dicionário
                                'nome': nome,
                                'fabricante': fabricante,
                                'valor': valor}
            lista_peca.append(dicionario_pecas.copy()) # Finalizando adição da cópia dos dados
            print("\n Peça número {} cadastrada com sucesso!".format(cod)) # Mensagem de sucesso
            break
        except:                   # Mensagem a ser exibida caso o usuário erre em alguma etapa desta função
            print("\n CADASTRO FALHOU! Tente Novamente.")
            continue   # Retorna ao início da função


def mostra_opcoes_consulta(): # Mostra as opções de consulta quando chamada
    print("\n")
    print("************** OPÇÕES DE CONSULTA **************")
    print("#----------------------------------------------#")
    print("|      DIGITE O NÚMERO DA OPÇÃO DESEJADA       |")
    print("#----------------------------------------------#")
    print("| 1 |       CONSULTAR TODAS AS PEÇAS           |")
    print("| 2 |     CONSULTAR UMA PEÇA POR CÓDIGO        |")
    print("| 3 |   CONSULTAR UMA PEÇA POR FABRICANTE      |")
    print("| 4 |       MOSTRAR TABELA DE OPÇÕES           |")
    print("| 5 |          CANCELAR CONSULTA               |")
    print("#----------------------------------------------#")
    print("\n")


def consulta_peca():  # Função consultarPeca, exigência 2
    while True:
        mostra_opcoes_consulta() # Mostra a tabela de opções de consulta
        try:
            opcao_escolhida = int(input("Digite o número de uma das opções da tabela: ")) # Recebe a opção escolhida
            if (opcao_escolhida == 1):
                print("--- CONSULTANDO TODAS AS PEÇAS ---")
                for peca in lista_peca:      # Consulta todas as peças
                    print("--------------------------------")
                    for key, value in peca.items():
                        print("{}: {}".format(key, value)) # Exibe as peças consultadas
                    print("--------------------------------")
                return   # Finaliza a consulta e volta para o programa principal
            elif (opcao_escolhida == 2):
                print("--- CONSULTANDO PEÇA POR CÓDIGO ---")
                cod_pesquisa = int(input("Digite o CÓDIGO da peça que você procura: "))
                # Recebe o código da peça para consulta
                for peca in lista_peca:
                    if (peca['codigo'] == cod_pesquisa): # Encontra a peça com o código fornecido
                        print("--------------------------------")
                        for key, value in peca.items():
                            print("{}: {}".format(key, value)) # Exibe as peças consultadas
                        print("--------------------------------")
                return     # Finaliza a consulta e volta para o programa principal
            elif (opcao_escolhida == 3):
                print("--- CONSULTANDO PEÇA POR FABRICANTE ---")
                fab_pesquisa = str(input("Digite o FABRICANTE da peça que você procura: "))
                # Recebe o fabricante da peça para consulta
                for peca in lista_peca:
                    if (peca['fabricante'] == fab_pesquisa):   # Encontra as peças com o fabricante fornecido
                        print("--------------------------------")
                        for key, value in peca.items():
                            print("{}: {}".format(key, value)) # Exibe as peças consultadas
                        print("--------------------------------")
                return      # Finaliza a consulta e volta para o programa principal
            elif (opcao_escolhida == 4):
                print("--- MOSTRANDO A TABELA DE OPÇÕES NOVAMENTE ---")
                continue # volta para o início da função, exibindo a tabela de opções novamente
            elif (opcao_escolhida == 5):
                print("CANCELANDO CONSULTA...")
                return  # Retorna ao programa principal, cancelando a consulta
            elif (opcao_escolhida == 0):
                print("O número 0 não é uma opção válida, por favor digite outro dígito.")
            else:           # Mensagem a ser exibida caso o usuário digite a opção inexistente 0
                print("Não entendi a opção desejada, por favor digite um dígito válido.")
        except:       # Mensagem a ser exibida caso o usuário erre em alguma etapa desta função
            print("A CONSULTA FALHOU! Tente novamente.")
            continue  # Retorna ao início da função


def exclui_peca():  # Função removePeca, exigência 3
    while True:
        try:
            opcao_excluir = int(input("Digite o CÓDIGO da peça que você deseja excluir: "))
            for peca in lista_peca:
                if (peca['codigo'] == opcao_excluir): # Encontra a peça com o código fornecido
                    lista_peca.remove(peca)  # Remove a peça encontrada na lista de peças
                    print("A peça de código {} foi deletada".format(opcao_excluir)) # Exibe uma mensagem de êxito
                    return # Retorna ao programa principal
        except:
            print("A EXCLUSÃO DE PEÇA FALHOU! Tente novamente.")
            continue # Repete o laço em caso de erro


# PROGRAMA PRINCIPAL

print("Bem-Vindo ao Controle de Estoque da Bicicletaria do aluno Daniel dos Santos Gama, RU: 4121047 \n")

codigo_peca = int(0)
lista_peca = []

while True:
    mostra_opcoes() # Exibe as opções iniciais do programa
    try:
        opcao = int(input("Digite a opção desejada aqui: ")) # Recebe a opção escolhida pelo usuário
    except:
        print("Valor não numérico, por favor digite uma opção válida")  # Exibe mensagem de erro, valor não numérico
        continue # Reinicia o laço
    if (opcao == 5):        # Encerra o programa
        print("Encerrando o programa...")
        break
    valida_opcao(opcao)  # Envia a opção escolhida para a função "valida_opção"
    continue # Reinicia o laço principal
