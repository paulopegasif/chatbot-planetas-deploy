from pandas import DataFrame, read_excel
from dados.sistema_solar import dados

# def carregar_conhecimento_em_texto(arquivo='dados\planetas.xlsx'):
#     df = read_excel(arquivo)
#     texto_base = ""
#     for _, row in df.iterrows():
#         texto_base += f"{row['Planeta']}: {row['Descrição']}\n"
#     return texto_base.strip()

def carregar_conhecimento_em_texto():
    texto_base: str = ''
    for key, value in dados.items():
        texto_base += f"{key}: {value}\n"
    return texto_base.strip()
