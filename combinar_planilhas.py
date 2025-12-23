import os
import pandas as pd
import csv

# Caminhos
PASTA_INPUT = "input"  # Pasta onde os CSVs/XLSXs de entrada estão
PASTA_OUTPUT = "output"
ARQUIVO_COMBINADO = os.path.join(PASTA_OUTPUT, "planilha_combinada.csv")

# Garante que a pasta de saída existe
os.makedirs(PASTA_OUTPUT, exist_ok=True)

# ⭐️ MUDANÇA 1: Lista de TODAS as colunas que ESPERAMOS encontrar nos arquivos de ENTRADA.
colunas_entrada_esperadas = [
    'SMARTCODE', 'DOCUMENTO', 'CNPJ', 'RazaoSocial', 'NomeFantasia', 
    'SituacaoCadastral', 'DataAbertura', 'NaturezaJuridica', 'CapitalSocial', 
    'AtividadePrincipal', 'Logradouro', 'Numero', 'Complemento', 'Bairro', 
    'Municipio', 'UF', 'EnderecoCompleto', 'TELEFONE', 'Telefone', 'Email', 
    'ENRIQUECIMENTO', 'FLAGDISPO', 'TIPO_BLOQUEIO_TELEFONE', 'Fonte'
]

# ⭐️ MUDANÇA 2: Lista das colunas FINAIS que queremos na saída, na ordem desejada.
colunas_saida = [
    'CNPJ',
    'RazaoSocial',
    'EnderecoCompleto',
    'Email',
    'SituacaoCadastral',
    'DataAbertura',
    'NaturezaJuridica',
    'CapitalSocial',
    'ENRIQUECIMENTO',
    #'Operadora', # Coluna Operadora não existe na sua planilha de entrada, será criada.
    'Telefone'
]


# Lista para armazenar os DataFrames válidos
todos_dfs = []

# Percorre todas as subpastas da PASTA_INPUT
print(f"Buscando arquivos CSV e XLSX na pasta '{PASTA_INPUT}' e subpastas...")

for raiz, _, arquivos in os.walk(PASTA_INPUT):
    for nome_arquivo in arquivos:
        caminho_arquivo = os.path.join(raiz, nome_arquivo)
        nome_arquivo_lower = nome_arquivo.lower()
        df = None # Variável para armazenar o DataFrame lido

        if not (nome_arquivo_lower.endswith(".csv") or nome_arquivo_lower.endswith(".xlsx")):
             continue # Ignora arquivos que não são CSV ou XLSX

        try:
            # 1. Leitura do arquivo
            if nome_arquivo_lower.endswith(".csv"):
                df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8-sig', dtype=str)
            elif nome_arquivo_lower.endswith(".xlsx"):
                df = pd.read_excel(caminho_arquivo, sheet_name=0, dtype=str)

            # 2. Limpeza dos nomes das colunas e verificação da estrutura
            df.columns = df.columns.str.strip()
            
            # Garante que as colunas de ENTRADA estão presentes e na ordem (ou similar)
            if list(df.columns) != colunas_entrada_esperadas:
                print(f"⚠️ Ignorado '{nome_arquivo}': As colunas de entrada não coincidem com as esperadas.")
                print(f"   Colunas encontradas: {list(df.columns)}")
                continue

            # 3. Tratamento e seleção de colunas
            
            # Renomeia a coluna 'TELEFONE' (vazia na sua amostra) para 'Operadora'
            # Se você tiver a operadora em outro campo, ajuste o rename.
            # Caso a coluna Operadora não exista, crie ela vazia se necessário
            if 'Operadora' not in df.columns:
                 # Criando a coluna 'Operadora' vazia (ou baseada em 'TELEFONE' que estava vazio)
                 # Se 'TELEFONE' é vazio, vamos criar 'Operadora' vazia.
                 df['Operadora'] = '' 
            
            # Seleciona apenas as colunas de SAÍDA na ordem correta
            df = df[colunas_saida]
            
            print(f"✅ Arquivo '{nome_arquivo}' lido e processado com sucesso.")
            todos_dfs.append(df)

        except Exception as e:
            print(f"❌ Erro ao ler '{nome_arquivo}': {e}")


# Junta todos os DataFrames
if todos_dfs:
    df_combinado = pd.concat(todos_dfs, ignore_index=True)

    # Salva o arquivo combinado usando delimitador TABULAÇÃO (\t), sem aspas
    df_combinado.to_csv(
        ARQUIVO_COMBINADO,
        sep='\t',
        index=False,
        encoding='utf-8',
        quoting=csv.QUOTE_NONE,
        escapechar='\\'
    )

    print(f"\n✅ Arquivo combinado salvo em: {ARQUIVO_COMBINADO}")
    print(f"📈 Total de linhas combinadas: {len(df_combinado)}")
else:
    print("\n⚠️ Nenhum arquivo válido encontrado para combinar.")

print("\n🏁 Processamento finalizado.")