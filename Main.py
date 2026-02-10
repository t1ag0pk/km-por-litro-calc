# Desenvolvido por mim durante o primeiro semestre da faculdade
# Basicamente não sabia utilizar nem criar funçoes mas fiz funcionar
# Chegou a hora de colocar no git hub e melhora-lo


from datetime import datetime, timedelta

dia_abastecimento_inicial= (input("\ninforme o dia do inicio do controle de abastecimento, formato(dd/mm/aaaa):"))
km_abastecimento_inicial = int(input("informe a quantidade de km rodados do dia do inicio do controle de abastecimento:"))


dia_abastecimento_bonus = dia_abastecimento_inicial
dia_abastecimento_bonusX = datetime.strptime(dia_abastecimento_bonus, "%d/%m/%Y") 
km_abastecimento_inicial_bonus = km_abastecimento_inicial
litros_bonus = 0

dia_abastecimento_final= (input("informe o dia do final do controle de abastecimento, formato(dd/mm/aaaa):"))
km_abastecimento_final = int(input("informe a quantidade de km rodados do dia do final do controle de abastecimento:"))

litros = float(input("digite quantos litros foram abastecidos:"))
litros_bonus = litros_bonus + litros




dia_abastecimento_inicialX = datetime.strptime(dia_abastecimento_inicial , "%d/%m/%Y") 
dia_abastecimento_finalX = datetime.strptime(dia_abastecimento_final , "%d/%m/%Y")

total_dias_rodados = dia_abastecimento_finalX - dia_abastecimento_inicialX
km_rodados = km_abastecimento_final - km_abastecimento_inicial
media = km_rodados/litros

#saida
print(f"\nDurante o período do dia {dia_abastecimento_inicial} até o dia {dia_abastecimento_final}:\nPassaram {total_dias_rodados.days} dias;\nUsou {litros} L de combustível;\nVocê rodou {km_rodados} Kms;\nCom uma média de {media:.2f}Km/L.\n")


pergunta = int(input("quer colocar os dados do próximos mês?\n0 = Não\n1 = Sim\n"))

while pergunta == 1:
    
    ultimo_dia_informado = dia_abastecimento_final
    ultimo_dia_informadoX = dia_abastecimento_finalX
    ultimo_km_informado = km_abastecimento_final

    dia_abastecimento_inicial = ultimo_dia_informado
    dia_abastecimento_inicialX = ultimo_dia_informadoX

    dia_abastecimento_final= (input("\ninforme o dia do final do controle de abastecimento, formato(dd/mm/aaaa):"))
    dia_abastecimento_finalX = datetime.strptime(dia_abastecimento_final , "%d/%m/%Y")

    km_abastecimento_inicial = ultimo_km_informado
    km_abastecimento_final = int(input("informe a quantidade de km rodados do dia do final do controle de abastecimento:"))

    litros = float(input("digite quantos litros foram abastecidos:"))
    litros_bonus = litros_bonus + litros

    total_dias_rodados = dia_abastecimento_finalX - dia_abastecimento_inicialX
    km_rodados = km_abastecimento_final - km_abastecimento_inicial
    media = km_rodados/litros

    print(f"\nDurante o período do dia {dia_abastecimento_inicial} até o dia {dia_abastecimento_final}:\nPassaram {total_dias_rodados.days} dias;\nUsou {litros} L de combustível;\nVocê rodou {km_rodados} Kms;\nCom uma média de {media:.2f}Km/L.\n")
    pergunta = int(input("quer colocar os dados do próximos mês?\n0 = Não\n1 = Sim\n"))


km_rodados_bonus = km_abastecimento_final - km_abastecimento_inicial_bonus
media_bonus = km_rodados_bonus/litros_bonus
total_dias_rodados_bonus = dia_abastecimento_finalX - dia_abastecimento_bonusX
print(f"\nBônus:\nDurante o período do dia {dia_abastecimento_bonus} até o dia {dia_abastecimento_final}:\nPassaram {total_dias_rodados_bonus.days} dias;\nUsou {litros_bonus:.2f}L de combustível;\nVocê rodou {km_rodados_bonus} Kms;\nCom uma média de {media_bonus:.2f}Km/L.\n")
