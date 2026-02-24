from database import salvar_abastecimento, buscar_dados, busca_por_id, excluir_dados
from datetime import datetime, timedelta

class Cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    CIANO = '\033[96m'
    RESET = '\033[0m' 

#entradas

def verificar_entrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            if valor <= 0:
                print(f"{Cor.VERMELHO}Erro: A quantidade deve ser maior que zero.{Cor.RESET}")
                continue 
            else:
                return valor
        except ValueError:
            print(f"{Cor.VERMELHO}digite apenas números{Cor.RESET}")

def pedir_data():
    while True:
        try:
            entrada = input(f"Informe o dia do abstecimento {Cor.AMARELO}(dd/mm/aaaa):{Cor.RESET} ")
            return datetime.strptime(entrada, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print(f"{Cor.VERMELHO}Formato inválido! Use dd/mm/aaaa.{Cor.RESET}")

def pedir_km():
    while True:
        try:
            v = int(input("Informe a quilometragem total do dia do abastecimento: "))
            if v < 0: raise ValueError
            return v
        except ValueError:
            print(f"{Cor.VERMELHO}Digite um número inteiro positivo.{Cor.RESET}")

def adicionar_dados():
    data = pedir_data()
    kms = pedir_km()
    valor_litro = verificar_entrada("Informe o valor por litro: ")
    litros = verificar_entrada("Informe quantos litros foram abastecidos: ")

    salvar_abastecimento(data, kms, valor_litro, litros)
    print(f"{Cor.VERDE}Informações salvas{Cor.RESET}")


#processamento / saída

def exibir_relatorio_completo():
    dados = buscar_dados("ORDER BY data ASC")
    
    if not dados:
        print(f"{Cor.VERMELHO}Nenhum dado encontrado.{Cor.RESET}")
        return

    print(f"\n{Cor.AZUL}{'ID':<4} {'Data':^12} {'KM':^11} {'Preço/L':^8} {'Litros':^10} {'R$ Total':^10}{Cor.RESET}")
    print("-" * 60)
    
    for registro in dados:
        id_b, data_b, km_b, v_l, litros_b, v_t = registro
        data = datetime.strptime(data_b, "%Y-%m-%d").strftime("%d/%m/%Y")
        print(f"{id_b:<4} {data:^12} {km_b:^11.0f} {v_l:^8.2f} {litros_b:^10.3f} {v_t:^10.2f}")

def calcular_consumo(registro):

    dados = buscar_dados("ORDER BY data ASC") 
    if len(dados) == 1:
        print(f"{Cor.RESET}Você não possui dados suficientes para fazer o cálculo.\núnico abastecimento encontrado é:{Cor.RESET}")
        exibir_relatorio_completo()
        return
    
    elif len(dados) == 0:
        print(f"{Cor.VERMELHO}Você não possui dados suficientes para fazer o cálculo.\nnenhum abastecimento encontrado{Cor.RESET}")
        return
    
    elif registro == "ultimo":
        # indíces negativos são os ultimos que foram adicionados ao banco
        id_u, data_u, km_u, pl_u, litros_u, vt_u = dados[-1]
        id_p, data_p, km_p, pl_p, litros_p, vt_p = dados[-2]

        distancia = km_u - km_p
        consumo_medio = distancia / litros_u
        m_valor = pl_p - pl_u
        if m_valor == 0:
            textov = f"mesmo valor"
        elif m_valor > 0:
            textov = f"abaixou: {m_valor:.2f}"
        else:
            textov = f"subiu: {abs(m_valor):.2f}"

        data_objeto_u = datetime.strptime(data_u, "%Y-%m-%d")
        data_objeto_p = datetime.strptime(data_p, "%Y-%m-%d")
        data_formatada_u = datetime.strptime(data_u, "%Y-%m-%d").strftime("%d/%m/%Y")
        data_formatada_p = datetime.strptime(data_p, "%Y-%m-%d").strftime("%d/%m/%Y")
        dias_percorridos = (data_objeto_u - data_objeto_p).days

        print(f"\n{Cor.AZUL}{'Data':^12} {'KM':^11} {'Preço/L':^8} {'Litros':^10} {'R$ Total':^10}{Cor.RESET}")
        print("-" * 54)

        # Print do penúltimo (-2)
        print(f"{data_formatada_p:^12} {km_p:^11.0f} {pl_p:^8.2f} {litros_p:^10.3f} {vt_p:^10.2f}")
        # Print do último (-1)
        print(f"{data_formatada_u:^12} {km_u:^11.0f} {pl_u:^8.2f} {litros_u:^10.3f} {vt_u:^10.2f}")

        print(f"\n{Cor.CIANO}{'Dias Percorridos':^20} {'KM Rodados':^11} {'Preço':^12} {'Média Km/l':^10}{Cor.RESET}")
        print("-" * 56)
        print(f"{dias_percorridos:^20} {distancia:^11.0f} {textov:^12} {consumo_medio:^10.2f}")



    elif registro == "todos":
        for i in range(1, len(dados)):
        
            #o atual (i) e o anterior (i - 1)
            id_u, data_u, km_u, pl_u, litros_u, vt_u = dados[i]
            id_p, data_p, km_p, pl_p, litros_p, vt_p = dados[i-1]

            distancia = km_u - km_p
            consumo_medio = distancia / litros_u

            m_valor = pl_p - pl_u
            if m_valor == 0:
                textov = f"mesmo valor"
            elif m_valor > 0:
                textov = f"abaixou: {m_valor:.2f}"
            else:
                textov = f"subiu: {abs(m_valor):.2f}"

            data_objeto_u = datetime.strptime(data_u, "%Y-%m-%d")
            data_objeto_p = datetime.strptime(data_p, "%Y-%m-%d")
            data_formatada_u = datetime.strptime(data_u, "%Y-%m-%d").strftime("%d/%m/%Y")
            data_formatada_p = datetime.strptime(data_p, "%Y-%m-%d").strftime("%d/%m/%Y")
            dias_percorridos = (data_objeto_u - data_objeto_p).days
        

            if i == 1:
                print(f"\n{Cor.CIANO}{"Data":^12}{'Dias Percorridos':^20} {'KM Rodados':^11} {'Preço':^12} {'Média Km/l':^10}{Cor.RESET}")
                print("-" * 68)

            print(f"{data_formatada_u:^12}{dias_percorridos:^20} {distancia:^11.0f} {textov:^12} {consumo_medio:^10.2f}")



    elif registro == "total":
        id_u, data_u, km_u, pl_u, litros_u, vt_u = dados[-1]
        id_p, data_p, km_p, pl_p, litros_p, vt_p = dados[0]

        litros_totais = sum(r[4] for r in dados[1:])
        distancia = km_u - km_p
        consumo_medio = distancia / litros_totais
        m_valor = pl_p - pl_u
        
        if m_valor == 0:
            textov = f"mesmo valor"
        elif m_valor > 0:
            textov = f"abaixou: {m_valor:.2f}"
        else:
            textov = f"subiu: {abs(m_valor):.2f}"

        data_objeto_u = datetime.strptime(data_u, "%Y-%m-%d")
        data_objeto_p = datetime.strptime(data_p, "%Y-%m-%d")
        data_formatada_u = datetime.strptime(data_u, "%Y-%m-%d").strftime("%d/%m/%Y")
        data_formatada_p = datetime.strptime(data_p, "%Y-%m-%d").strftime("%d/%m/%Y")
        dias_percorridos = (data_objeto_u - data_objeto_p).days

    
        print(f"\n{Cor.CIANO}{"Inicio":^12}{"Final":^12}{'Dias Percorridos':^20} {'KM Rodados':^11} {'Preço':^12} {'Média Km/l':^10}{Cor.RESET}")
        print("-" * 80)
        print(f"{data_formatada_p:^12}{data_formatada_u:^12}{dias_percorridos:^20} {distancia:^11.0f} {textov:^12} {consumo_medio:^10.2f}")

def excluir_abastecimento():

    print(f"{Cor.AMARELO}Qual dos seguintes abastecimentos você deseja deletar?: {Cor.RESET}")
    exibir_relatorio_completo()
    print()

    while True: #pegar o id de forma segura recebendo um número
        try:
            id_usuario = int(input(f"Informe o ID referente aos dados que você deseja deletar: "))
            if id_usuario <= 0:
                print(f"{Cor.VERMELHO}Erro: O número do ID deve ser maior que zero.{Cor.RESET}")
                continue 
            else:
                break
        except ValueError:
            print(f"{Cor.VERMELHO}digite apenas números{Cor.RESET}")
    
    dados_do_abastecimento = busca_por_id(id_usuario)
    if not dados_do_abastecimento:
        print(f"{Cor.AMARELO}\nO valor de id informado não foi encontrado no banco, por favor, tente novamente.{Cor.RESET}")
        print(f"{Cor.VERMELHO}Operação cancelada!{Cor.RESET}")
        return
    
    # print dos dados a serem excluídos 
    print(f"{Cor.AMARELO}Dados a serem deletados:{Cor.RESET}")
    print(f"\n{Cor.AZUL}{'ID':<4} {'Data':^12} {'KM':^11} {'Preço/L':^8} {'Litros':^10} {'R$ Total':^10}{Cor.RESET}")
    print("-" * 60)
    id_b, data_b, km_b, v_l, litros_b, v_t = dados_do_abastecimento
    data = datetime.strptime(data_b, "%Y-%m-%d").strftime("%d/%m/%Y")
    print(f"{id_b:<4} {data:^12} {km_b:^11.0f} {v_l:^8.2f} {litros_b:^10.3f} {v_t:^10.2f}")



    print(f"{Cor.CIANO}\nDeseja confirmar a opção de cancelamento?{Cor.RESET}")

    while True: #pegar a confirmação de forma segura recebendo um número
        try:
            confirmar = int(input(f"Digite 0 para {Cor.VERDE}CONFIRMAR{Cor.RESET}\nDigite 1 para {Cor.VERMELHO}CANCELAR\n{Cor.RESET}"))
            if confirmar not in [0, 1]:
                print(f"{Cor.VERMELHO}Erro: Use apenas 0 ou 1{Cor.RESET}")
                continue 
            else:
                break
        except ValueError:
            print(f"{Cor.VERMELHO}digite apenas números{Cor.RESET}")

    if confirmar == 0:
        execute = excluir_dados(id_usuario)
        if not execute:
            print(f"{Cor.AMARELO}Ocorreu algum erro, não foi possível concluir a operação\n{Cor.VERMELHO}Operação falhou{Cor.RESET}")
        print(f"{Cor.AMARELO}Operação finalizada com sucesso os dados foram excluídos.\n{Cor.VERDE}Operação finalizada.{Cor.RESET}")
    else:
        print(f"{Cor.VERMELHO}Operação cancelada!{Cor.RESET}")


def menu():
    while True:
        print(f"\n{Cor.AZUL}===== SISTEMA KM POR LITRO ====={Cor.RESET}")
        print("1. Cadastrar Novo Abastecimento")
        print("2. Ver Histórico de Abastecimentos Completo")
        print("3. Ver Média de Consumo do último Mês")
        print("4. Ver Média de Consumo de Todos os Meses")
        print("5. Ver Média de Consumo Entre o Primeiro e Último Abastecimento")
        print("6. Remover Dados de Abastecimento")
        print("7. Sair")
        
        opcao = input(f"\n{Cor.AMARELO}Escolha uma opção: {Cor.RESET}")

        if opcao == "1":
            adicionar_dados()
        elif opcao == "2":
            exibir_relatorio_completo()
        elif opcao == "3":
            calcular_consumo(registro="ultimo")
        elif opcao == "4":
            calcular_consumo(registro="todos")
        elif opcao == "5":
            calcular_consumo(registro="total")
        elif opcao == "6":
            excluir_abastecimento() 
        elif opcao == "7":
            print(f"{Cor.VERDE}Sistema finalizado com sucesso!{Cor.RESET}")
            break
        else:
            print(f"{Cor.VERMELHO}Opção inválida!{Cor.RESET}")

# Única linha fora de funções para iniciar tudo:
if __name__ == "__main__":
    menu()