# 🗂️ Projeto de Combinação de CSVs

Este projeto automatiza a leitura, validação e combinação de arquivos CSV em uma única planilha consolidada.

## 🚀 Funcionalidade
- Percorre a pasta `input` e todas as suas subpastas.
- Lê arquivos CSV com separador `;` e codificação `utf-8-sig`.
- Valida se as colunas estão na ordem correta:
  - `CNPJ`
  - `RazaoSocial`
  - `EnderecoCompleto`
  - `Email`
  - `SituacaoCadastral`
  - `DataAbertura`
  - `NaturezaJuridica`
  - `CapitalSocial`
  - `ENRIQUECIMENTO`
  - `Operadora`
  - `Telefone`
- Ignora arquivos com estrutura diferente.
- Concatena todos os arquivos válidos em um único DataFrame.
- Exporta o resultado para `output/planilha_combinada.csv` no formato **TSV** (tabulação como delimitador).

## 📂 Estrutura de Pastas

projeto-csv-combinador/ │── input/   
Pasta com os arquivos CSV de entrada│── input/    
Pasta onde será gerado o arquivo combinado │── output/   
Código principal  │── script.py   
Documentação │── README.md    



## ▶️ Como Executar
1. Instale as dependências:
   ```bash
   pip install pandas

2 - Coloque seus arquivos CSV na pasta input/.

3 - Execute o script: python script.py

4 - O resultado estará em:
output/planilha_combinada.csv

   
