import pandas as pd
import os

# Definir o diretório onde estão os arquivos CSV
diretorio = "csv_files"

# Obter uma lista de todos os arquivos CSV no diretório
arquivos_csv = [f for f in os.listdir(diretorio) if f.endswith(".csv")]

# Inicializar um objeto ExcelWriter
with pd.ExcelWriter("Racional 04-2024.xlsx") as writer:
    # Iterar sobre a lista de arquivos CSV
    for arquivo_csv in arquivos_csv:
        nome_arquivo = os.path.splitext(arquivo_csv)[0]
        nome_arquivo = "MENSAL - " + nome_arquivo.upper()

        # Ler o arquivo CSV em um DataFrame
        dataFrame = pd.read_csv(os.path.join(diretorio, arquivo_csv))

        # Definir as colunas que você deseja migrar
        colunas = ["Work Item Type", "ID", "Title", "Assigned To", "UsedTime"]

        # Selecionar apenas as colunas desejadas
        dataFrame = dataFrame[colunas]

        # Verificar se o DataFrame está vazio
        if dataFrame.empty:
            print(
                f"O arquivo {arquivo_csv} está vazio ou não contém as colunas desejadas."
            )
            continue

        # Calcular a soma da coluna "UsedTime"
        total = dataFrame["UsedTime"].sum()

        # Criar uma linha totalizadora com a soma
        total_row = pd.DataFrame({"UsedTime": [total]})

        # Adicionar a linha totalizadora ao DataFrame
        dataFrame = pd.concat([dataFrame, total_row])

        # Adicionar o DataFrame ao objeto ExcelWriter como uma nova aba
        dataFrame.to_excel(writer, sheet_name=nome_arquivo, index=False)
