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
print("✅ Análise Concluída!")
print("="*50 + "\n")


print("📈 RESUMO ESTATÍSTICO:\n")
print(df[['Idade', 'Peso', 'Altura', 'IMC']].describe().round(2))
