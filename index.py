import os
import pandas as pd

from src.csv_reader import read_csv_file
from src.excel_writer import write_to_excel
from src.environments import csv_directory, csv_files_list


def main():
    aggregated_stats = {"Nome": [], "Total de Horas": []}
    dataframes = {}

    for csv_file in csv_files_list:
        file_name = os.path.splitext(csv_file)[0]
        monthly_file_name = "MENSAL - " + file_name.upper()

        print("Processing file:", file_name)

        csv_file_path = os.path.join(csv_directory, csv_file)
        data_frame = read_csv_file(csv_file_path)

        total = data_frame["UsedTime"].sum()
        total_row = pd.DataFrame({"UsedTime": [total]})
        data_frame = pd.concat([data_frame, total_row])

        dataframes[monthly_file_name] = data_frame
        aggregated_stats["Nome"].append(file_name)
        aggregated_stats["Total de Horas"].append(total)

    write_to_excel(dataframes, aggregated_stats)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o arquivo Excel: {str(e)}")
