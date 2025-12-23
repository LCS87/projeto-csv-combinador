# projeto-csv-combinador

Ferramenta simples para buscar CSVs em `input/` (e subpastas), validar esquema e combinar em um único arquivo em `output/planilha_combinada.csv`.

## Objetivo
Combinar várias planilhas CSV geradas por etapas anteriores (por exemplo: saídas de processos de consulta) em um único arquivo tab-delimitado.

## Pré-requisitos
- Python 3.8+ (recomendado 3.10/3.11)
- Criar um ambiente virtual e instalar dependências

## Instalação (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Estrutura esperada
- `input/` : pasta onde o script procura arquivos `.csv` (pesquisa recursiva)
- `output/`: pasta onde o arquivo combinado será salvo

### Colunas esperadas
O script espera que os CSVs tenham exatamente as colunas (mesma ordem):

```
CNPJ
RazaoSocial
EnderecoCompleto
Email
SituacaoCadastral
DataAbertura
NaturezaJuridica
CapitalSocial
ENRIQUECIMENTO
Operadora
Telefone
```

Se algum arquivo tiver esquema diferente ele será ignorado e mostrado no log.

## Uso
```powershell
# Ative o venv
.\.venv\Scripts\Activate.ps1

# Executar
python combinar_planilhas.py
```

O arquivo combinado será salvo em `output/planilha_combinada.csv` (delimitador `\t`).

## Observações importantes
- O script lê CSVs usando `sep=';'` e `encoding='utf-8-sig'`. Ajuste se seus arquivos usarem outro separador/encoding.
- As dependências atuais estão travadas em `requirements.txt` para reprodutibilidade.
- Melhorias recomendadas: adicionar CLI (`argparse`/`typer`), logs mais estruturados, suporte a schema flexível, processamento por `chunksize` para arquivos grandes, e testes automatizados.

## Contato
Abra uma issue ou PR neste repositório com melhorias ou bugs encontrados.
