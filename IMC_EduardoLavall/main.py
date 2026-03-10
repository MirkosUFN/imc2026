"""
IMC Analysis - Eduardo Lavall
Análise de Dados com Cálculo de IMC
"""

import pandas as pd
import os
from pathlib import Path


script_dir = Path(__file__).parent
csv_path = script_dir / "dados_pessoas.csv"


df = pd.read_csv(csv_path)

stats = {
    "Média de idade": df["Idade"].mean(),
    "Menor peso": df["Peso"].min(),
    "Maior altura": df["Altura"].max()
}


df["IMC"] = df["Peso"] / (df["Altura"] ** 2)
stats["IMC dominante"] = df["IMC"].round(1).mode()[0]


# ─── Classificação de IMC ────────────────────────────────────────────────────
# Regra de negócio: cada pessoa recebe uma categoria com base no valor do IMC
# calculado acima, seguindo a tabela da OMS:
#
#   < 18.5          → Abaixo do peso
#   18.5 a 24.9     → Normal
#   25.0 a 29.9     → Sobrepeso
#   ≥ 30.0          → Obesidade
#
# A função abaixo recebe um valor de IMC e retorna a categoria correspondente.

def classificar_imc(imc: float) -> str:
    """Retorna a categoria de IMC conforme os critérios da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Aplica a classificação em cada linha e armazena na coluna 'Classificação'
df["Classificação"] = df["IMC"].apply(classificar_imc)
# ─────────────────────────────────────────────────────────────────────────────


# ─── Contagem de Vogais no Nome ───────────────────────────────────────────────
# Regra de negócio: conta quantas vogais (a, e, i, o, u) existem no nome
# completo de cada pessoa, ignorando maiúsculas/minúsculas e acentos comuns.
# Útil para análises linguísticas ou simplesmente enriquecer o dataset.

def contar_vogais(nome: str) -> int:
    """Retorna o número de vogais no nome, incluindo vogais acentuadas."""
    vogais = set("aeiouáéíóúâêîôûãõàèìòùäëïöü")
    return sum(1 for letra in nome.lower() if letra in vogais)

# Aplica a contagem para cada nome e armazena na coluna 'Vogais_Nome'
df["Vogais_Nome"] = df["Nome"].apply(contar_vogais)
# ─────────────────────────────────────────────────────────────────────────────


# ─── Relação Idade / IMC ──────────────────────────────────────────────────────
# Regra de negócio: calcula a razão entre a idade e o IMC da pessoa.
# Um valor mais alto indica que a pessoa tem mais idade proporcionalmente
# ao seu IMC — pode ser utilizado para identificar perfis como pessoas
# mais velhas com IMC baixo, ou jovens com IMC elevado.
# Resultado arredondado em 2 casas decimais para facilitar a leitura.

df["Relação_Idade_IMC"] = (df["Idade"] / df["IMC"]).round(2)
# ─────────────────────────────────────────────────────────────────────────────


print("\n" + "="*50)
print("📊 ANÁLISE DE DADOS - IMC")
print("="*50 + "\n")

for chave, valor in stats.items():
    if isinstance(valor, float):
        print(f"✓ {chave}: {valor:.2f}")
    else:
        print(f"✓ {chave}: {valor}")

print("\n" + "="*50)
print("📋 TABELA COM IMC CALCULADO")
print("="*50 + "\n")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

print(df.to_string(index=False))

print("\n" + "="*50)
print("🏷️  DISTRIBUIÇÃO POR CLASSIFICAÇÃO DE IMC")
print("="*50 + "\n")

# Conta quantas pessoas estão em cada categoria e exibe em ordem lógica
ordem_categorias = ["Abaixo do peso", "Normal", "Sobrepeso", "Obesidade"]
contagem = df["Classificação"].value_counts()

for categoria in ordem_categorias:
    qtd = contagem.get(categoria, 0)
    percentual = (qtd / len(df)) * 100
    print(f"  {categoria:<18} {qtd:>2} pessoa(s)  ({percentual:.1f}%)")

print("\n" + "="*50)
print("✅ Análise Concluída!")
print("="*50 + "\n")


print("📈 RESUMO ESTATÍSTICO:\n")
print(df[['Idade', 'Peso', 'Altura', 'IMC', 'Vogais_Nome', 'Relação_Idade_IMC']].describe().round(2))
