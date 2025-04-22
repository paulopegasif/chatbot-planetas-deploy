from pandas import DataFrame, read_excel

def carregar_conhecimento_em_texto(arquivo='dados\planetas.xlsx'):
    df = read_excel(arquivo)
    texto_base = ""
    for _, row in df.iterrows():
        texto_base += f"{row['Planeta']}: {row['Descrição']}\n"
    return texto_base.strip()
