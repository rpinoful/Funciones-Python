from csv import DictReader, reader
from pprint import pprint

def ler_csv(arquivo:str) ->list:
    """
    Recebe um arquivo de produtos csv e armazena em uma lista

    Args:
        arquivo (str): nome ou path do arquivo

    Returns:
        list: lista onde tem todos os produtos
    """
    
    with open(arquivo, 'r',encoding='utf-8') as f:
        reader = DictReader(f)
        produtos = [p for p in reader]
            
    
    return produtos


def filtrar_produtos_entregue(lista:list[dict]) -> list[dict]:
    nao_entregue = [produto for produto in lista if produto.get("Entregue") =='True']
    return nao_entregue
        
    


def somar_valores_produtos(lista:list[dict]) -> list[dict]:
    valor_total = sum(float(produto['preco']) for produto in lista)
    return valor_total






