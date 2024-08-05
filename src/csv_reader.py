import csv
import pandas as pd
from .environments import columns


def read_csv_file(csv_file_path):
    with open(csv_file_path, "r", encoding="utf-8-sig") as file:
        # Ler o arquivo CSV
        csv_data = list(csv.reader(file))

        # Criar um dicionário com os cabeçalhos como chaves
        csv_headers = [header.strip() for header in csv_data[0]]
        data_dict = {header: [] for header in csv_headers}

        # Preencher o dicionário com os valores
        for row in csv_data[1:]:
            for i, value in enumerate(row):
                data_dict[csv_headers[i]].append(value.strip())

        # Criar uma cópia das chaves do dicionário
        selected_keys = list(data_dict.keys())

        # Remover registros do dicionário que não estão nas colunas
        for column_key in selected_keys:
            if column_key not in columns:
                del data_dict[column_key]

        # Criar um dicionário ordenado com as colunas desejadas
        sorted_dict = {column: data_dict[column] for column in columns}
        sorted_dict["UsedTime"] = pd.to_numeric(sorted_dict["UsedTime"]).tolist()

        # Criar uma planilha no arquivo Excel para cada arquivo CSV com os dados do dicionário ordenado
        return pd.DataFrame(sorted_dict)
