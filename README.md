# Azure DevOps - CSV to Excel

## Introdução

Esta aplicação foi desenvolvida para converter arquivos CSV exportados do Azure DevOps para Excel, proporcionando uma visualização mais amigável e facilitando a análise detalhada dos dados.

## Objetivo

Facilitar a conversão de arquivos CSV exportados do Azure DevOps para o formato Excel. A princípio, a aplicação é voltada para consolidar informações de Work Items, mas pode ser facilmente adaptada para outros tipos de dados.

## Proposta

Criar uma aplicação que permita ao usuário selecionar um ou mais arquivos CSV exportados do Azure DevOps e consolidar informações (como Horas, Tarefas, etc.) em um arquivo Excel.

## Tecnologias Utilizadas

- **Python 3.8**
- **Pandas**: Biblioteca poderosa para manipulação de dados.
- **Openpyxl**: Biblioteca para trabalhar com arquivos Excel.
- **CSV**: Módulo para ler e escrever arquivos CSV.

## Instalação

### Pré-requisitos

Certifique-se de ter o Python 3.8 instalado em sua máquina. Você pode verificar a versão do Python instalada com o comando:

```sh
python --version
```

### Passos para Instalação

1. Clone o repositório do projeto:

```sh
git clone https://github.com/muleroD/azure-devops-csv-to-excel-converter
cd azure-devops-csv-to-excel-converter
```

2. Crie um ambiente virtual:

```sh
python -m venv venv
source venv/bin/activate   # Para Windows, use: venv\Scripts\activate
```

3. Instale as dependências do projeto:

```sh
pip install -r requirements.txt
```

## Uso

### Estrutura do Projeto

```
.
├── data
│   ├── input
│   └── output
├── src
│   ├── csv_reader.py
│   ├── excel_writer.py
│   └── environments.py
├── requirements.txt
├── index.py
└── README.md
```

### Executando a Aplicação

1. Coloque os arquivos CSV que deseja converter na pasta `data/input`.
2. Realize as configurações necessárias no arquivo `environments.py`.
3. Execute o script principal:

```sh
python index.py
```

3. O arquivo Excel consolidado será gerado na pasta `data/output`.

### Detalhes dos Scripts

- **index.py**: Script principal que orquestra a leitura dos CSVs e a geração do arquivo Excel.
- **csv_reader.py**: Contém funções para ler e manipular os arquivos CSV.
- **excel_writer.py**: Contém funções para escrever os dados consolidados em um arquivo Excel.
- **environments.py**: Contém variáveis de ambiente e configurações do projeto.

## Exemplo de Uso

Aqui está um exemplo de como você pode usar a aplicação:

1. Adicione seus arquivos CSV exportados do Azure DevOps na pasta `data/input`.
2. Execute o script principal:

```sh
python index.py
```

3. Verifique o arquivo Excel consolidado gerado na pasta `data/output`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
