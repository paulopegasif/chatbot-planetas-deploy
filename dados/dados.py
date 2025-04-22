from dados.sistema_solar import dados

def carregar_conhecimento_em_texto():
    """
    Carrega o conhecimento contido no dicionário `dados` em formato de texto.

    Esta função itera sobre o dicionário `dados` e cria uma string concatenada, onde
    cada chave do dicionário é seguida por seu respectivo valor. O texto gerado é 
    formatado com cada par chave-valor em uma nova linha.

    Returns
    -------
    str
        A string formatada contendo o conhecimento extraído do dicionário `dados`, 
        onde cada linha segue o formato "chave: valor".

    Notes
    -----
    A função assume que a variável global `dados` está definida e é um dicionário,
    onde as chaves são de tipos imutáveis (como strings, números, etc.) e os valores 
    podem ser de qualquer tipo. Cada par chave-valor será convertido para string e 
    concatenado na variável `texto_base`.

    Example
    --------
    >>> dados = {'planeta': 'Terra', 'distancia': '149.6 milhões de km'}
    >>> carregar_conhecimento_em_texto()
    'planeta: Terra\ndistancia: 149.6 milhões de km'
    """
    texto_base: str = ''
    for key, value in dados.items():
        texto_base += f"{key}: {value}\n"
    return texto_base.strip()
