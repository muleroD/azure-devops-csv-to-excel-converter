import pandas as pd
import csv
import os

# Definir o diretório onde estão os arquivos CSV
diretorio = "csv_files/07-2024"

# Obter uma lista de todos os arquivos CSV no diretório
arquivos_csv = [f for f in os.listdir(diretorio) if f.endswith(".csv")]

# Definir as colunas que você deseja migrar
colunas = ["Work Item Type", "ID", "Title", "Assigned To", "UsedTime"]

try:
    with pd.ExcelWriter("Racional 07-2024.xlsx") as writer:

        # Criar um dicionário para armazenar os valores da aba CONSOLIDADO
        consolidado_dict = {"Nome": [], "Total de Horas": []}

        # Iterar sobre a lista de arquivos CSV
        for arquivo_csv in arquivos_csv:
            nome_arquivo = os.path.splitext(arquivo_csv)[0]
            nome_arquivo_mensal = "MENSAL - " + nome_arquivo.upper()

            print("Processando o arquivo:", nome_arquivo)

            csv_file_path = os.path.join(diretorio, arquivo_csv)

            with open(csv_file_path, "r", encoding="utf-8-sig") as arquivo:
                data = list(csv.reader(arquivo))

                # Criar um dicionário com os cabeçalhos como chaves
                cabecalhos = [cabecalho.strip() for cabecalho in data[0]]
                dicionario = {cabecalho: [] for cabecalho in cabecalhos}

                # Preencher o dicionário com os valores
                for linha in data[1:]:
                    for i, valor in enumerate(linha):
                        dicionario[cabecalhos[i]].append(valor.strip())

                # Criar uma cópia das chaves do dicionário
                chaves = list(dicionario.keys())

                # Remover registros do dicionário que não estão nas colunas
                for coluna in chaves:
                    if coluna not in colunas:
                        del dicionario[coluna]

                dicionario_ordenado = {coluna: dicionario[coluna] for coluna in colunas}
                dicionario_ordenado["UsedTime"] = pd.to_numeric(
                    dicionario_ordenado["UsedTime"]
                )

                # Criar uma planilha no arquivo Excel para cada arquivo CSV com os dados do dicionário ordenado
                dataFrame = pd.DataFrame(dicionario_ordenado)

                # Calcular a soma da coluna "UsedTime"
                total = dataFrame["UsedTime"].sum()

                # Criar uma linha totalizadora com a soma
                total_row = pd.DataFrame({"UsedTime": [total]})

                # Adicionar a linha totalizadora ao DataFrame
                dataFrame = pd.concat([dataFrame, total_row])

                dataFrame.to_excel(writer, sheet_name=nome_arquivo_mensal, index=False)

                # Adicionar os valores do CONSOLIDADO ao dicionário
                consolidado_dict["Nome"].append(nome_arquivo)
                consolidado_dict["Total de Horas"].append(total)

        # Criar um DataFrame com os valores do CONSOLIDADO
        consolidado = pd.DataFrame(consolidado_dict)

        # Adicionar a sheet "CONSOLIDADO" ao arquivo Excel
        consolidado.to_excel(writer, sheet_name="CONSOLIDADO", index=False)
except Exception as e:
    print(f"Ocorreu um erro ao gerar o arquivo Excel: {str(e)}")
