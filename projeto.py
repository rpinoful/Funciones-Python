from csv import DictReader, reader
from pprint import pprint

def ler_csv_novo(arquivo:str) ->list[dict]:  
    """
    Entrada: Nome do arquivo CSV
    Saída: Lista de dicionários com dados lidos
    """

    vendas = []
    
    with open(arquivo, 'r',encoding='utf-8') as f:
        reader = DictReader(f)
        for linha in reader:
            vendas.append(linha)
    return vendas



# 2 - Processar Dados:
#     Função: processar_dados
#     Entrada: Lista de dicionários
#     Saída: Dicionário processado conforme descrito

def processar_dados(produtos:dict[list]) ->dict[list]:
    produtos_requeridos = [produto for produto in produtos if produto['entregue']=='true']
    
    
    return produtos_requeridos




# 3-Calcular Vendas por Categoria:

#     Função: calcular_vendas_categoria
#     Entrada: Dicionário processado
#     Saída: Dicionário com total de vendas por categoria
def calcular_vendas_categoria(produtos:dict[list])-> dict:
    total_por_categoria = {}
    for produto in produtos:
        categoria = produto ['categoria']
        preco = float(produto['preco'])
        
        
        if produto ['categoria'] in total_por_categoria:
            total_por_categoria[categoria]+= preco
        
        
        else:
            total_por_categoria[categoria] = preco
    
    
    
    
    return total_por_categoria







# 1 - Lendo o arquivo
arquivo_csv = 'vendas2.csv'
dicionario_lista_produtos = ler_csv_novo(arquivo_csv)


# 2 - processando produtos que foram entregues e colocando em uma lista de dicionarios
produtos_entregues = processar_dados(dicionario_lista_produtos,)


#3 - Calcular vendas por categoria
total_vendas_categoria = calcular_vendas_categoria(produtos_entregues)
pprint(total_vendas_categoria)

