import pandas as pd
from pandas import DataFrame

def dataset_limpo() -> DataFrame:
    df = pd.read_csv("/home/julioccds/Documentos/app/bancodados.csv",sep=";",decimal=",")
    df = df.drop(0,axis=0)
    nomes_colunas = {
    "Unnamed: 0" : "Sigla",
    "Unnamed: 1" : "Código",
    "Unnamed: 2" : "Município",
    "Unnamed: 3" : "1991 (%)",
    "Unnamed: 4" : "2000 (%)",
    "Unnamed: 5" : "2010 (%)",
    "Unnamed: 6" : "2022 (%)",
    }
    df = df.rename(columns=nomes_colunas)
    df["Código"] = df["Código"].astype(int)
    colunas_anos = ["1991 (%)","2000 (%)","2010 (%)","2022 (%)"]
    df["Percentual Médio de não Alfabetizados"] = df[colunas_anos].mean(axis=1)
    df["Percentual Médio de Alfabetizados"] = 100 - df["Percentual Médio de não Alfabetizados"]
    return df



