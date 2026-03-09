# 📊 IMC Analysis - Eduardo Lavall

Aplicação standalone de análise de dados com cálculo de IMC.

## 📋 Descrição

Este é um projeto de análise de dados que:
- Lê dados de pessoas (nome, idade, peso, altura) de um arquivo CSV
- Calcula estatísticas: média de idade, menor peso, maior altura
- Calcula o **IMC (Índice de Massa Corporal)** para cada pessoa
- Exibe um resumo estatístico completo

## 🚀 Como Usar

### Opção 1: Executar com F5 (VS Code)
1. Abra `main.py` no VS Code
2. Pressione **F5** para executar

### Opção 2: Executar via Terminal
```bash
python main.py
```

## 📁 Arquivos

- **main.py** - Script principal da análise
- **dados_pessoas.csv** - Arquivo com dados das pessoas

## 📊 Saída

O script exibe:
- ✓ Estatísticas principais (média de idade, menor peso, maior altura, IMC dominante)
- ✓ Tabela com todos os dados + IMC calculado
- ✓ Resumo estatístico (count, mean, std, min, max, quartis)

## 🧮 Fórmula do IMC

```
IMC = Peso (kg) / Altura (m)²
```

Exemplo: Uma pessoa com 70kg e 1.75m tem IMC = 70 / (1.75²) ≈ 22.86

## 📌 Requisitos

- Python 3.8+
- pandas

## ✨ Características

✅ Executa standalone (sem servidor web)  
✅ Lê o CSV do mesmo diretório  
✅ Saída formatada e fácil de ler  
✅ Incluí resumo estatístico completo  
✅ Pronto para F5 no VS Code  

---

**Desenvolvido para:** Análise de Dados | Eduardo Lavall | 2026
