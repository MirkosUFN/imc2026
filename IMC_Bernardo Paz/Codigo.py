import pandas as pd

caminho = '/content/drive/MyDrive/Ciência de Dados/Pessoas.xlsx'
arquivo = pd.read_excel(caminho)

# Qual a media de idade?
media_idade = arquivo['Idade'].mean()
print(f"Média de idade: {media_idade:.2f} anos")

# Qual o menor peso?
menor_peso = arquivo['Peso'].min()
print(f"Menor peso: {menor_peso:.2f} kg")

# Qual a maior altura?
maior_altura = arquivo['Altura'].max()
print(f"Maior altura: {maior_altura:.2f} m")

# Criar a coluna IMC
arquivo['IMC'] = arquivo['Peso'] / (arquivo['Altura'] ** 2)

# Grupo IMC dominante
def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc <= 24.9:
        return 'Peso normal'
    elif 25.0 <= imc <= 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

arquivo['Grupo_IMC'] = arquivo['IMC'].apply(classificar_imc)

grupo_dominante = arquivo['Grupo_IMC'].mode()[0]
quantidade = (arquivo['Grupo_IMC'] == grupo_dominante).sum()

print("Visualização final da tabela:")
display(arquivo)

caminho_salvar = '/content/drive/MyDrive/Ciência de Dados/Pessoas_IMC_Atualizado.xlsx'
arquivo.to_excel(caminho_salvar, index=False)

print(f"DataFrame salvo com sucesso em: {caminho_salvar}")
