import pandas as pd
from datetime import datetime

total = 0.00
total_cheque = 0.00
total_dinheiro = 0.00
total_recibos = 0
cheques = []
recibos_detalhes = []

def recibos():
    global total, total_recibos
    while True:
        recibo_input = input("Digite o Valor do recibo (Ou pressione ENTER para finalizar): ")
        if recibo_input == "":
            break
        
        try:
            recibo = float(recibo_input)
            qtd = int(input("Quantidade de recibos: "))

        except ValueError:
            print("X Entrada inválida! Digite apenas números!")
            continue

        subtotal = recibo * qtd
        total += subtotal
        total_recibos += qtd
        recibos_detalhes.append({"Valor do Recibo": recibo, "Quantidade": qtd, "Valor Total": subtotal})
        
    return recibos_detalhes

def fechamento():
    global total_cheque, total_dinheiro
    while True:
        cheques_input = input('Digite o valor do cheque separados por virgula: ')
        if cheques_input:
            try:
                valores_cheques = [float(valor.strip()) for valor in cheques_input.split(",")]
                cheques.extend(valores_cheques)
                total_cheque = sum(cheques)
                break
            
            except ValueError:
                print("X Entrada inválida! Certifique-se de separar corretamente por vírgula!")
        else:
            break
            

    # Somar valores de dinheiro até o usuário pressionar Enter sem digitar nada pra finalizar
    print('Digite um valor em dinheiro um por vez, ou pressione ENTER sem nada para finalizar: ')
    while True:
        dinheiro_input = input('Valor em dinheiro: ')
        if dinheiro_input == "":
            break
        try:
            total_dinheiro += float(dinheiro_input)

        except ValueError:
            print("X Entrada Inválida! Digite apenas números.")
    
recibos()
fechamento()

# Criando DataFrame para os recibos
df_recibos = pd.DataFrame(recibos_detalhes)

# Criando um DataFrame para os totais
df_totais = pd.DataFrame({
    "Total Recibos": [total],
    "Total Cheques": [total_cheque],
    "Total Dinheiro": [total_dinheiro]
})

# Nome do Arquivo
arquivo_excel = "fechamento_caixa2.xlsx"
data_fechamento = datetime.now().strftime("%d-%m-%Y")

# Salvar no Excel

with pd.ExcelWriter(arquivo_excel, mode='w', engine="openpyxl") as writer:
    df_recibos.to_excel(writer, sheet_name=data_fechamento, index=False)
    df_totais.to_excel(writer, sheet_name=data_fechamento, startrow=len(df_recibos) + 2, index=False)

print(f"\nFechamento de Caixa Salvo! '{data_fechamento}' dentro do arquivo {arquivo_excel}!")