import os

# Definir o nome do arquivo Excel que será gerado
excel_export = os.path.join("data/output", "Racional.xlsx")

# Diretório onde os arquivos CSV estão localizados
csv_directory = "data/input"

# Obter uma lista de todos os arquivos CSV no diretório
csv_files_list = [f for f in os.listdir(csv_directory) if f.endswith(".csv")]

# Definir as colunas que você deseja migrar
columns = ["Work Item Type", "ID", "Title", "Assigned To", "UsedTime"]
