import pandas as np

#Criar um Dicionario com dados de alunos

dados = {
    "Nome " : ["Ana", "Bruno", "Carlos", "Diana"],
    "Idade" : [20, 22, 19, 21],
    "Nota" : [8.5, 7.0, 9.0, 8.0]
}

#Criar  DataFrame
df = pd.DataFrame (dados)
print(df)

print("\nEstatistica de Notas:")
print (df["Nota"].describe())