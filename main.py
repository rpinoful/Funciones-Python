from pprint import pprint

from etl import ler_csv,filtrar_produtos_entregue,somar_valores_produtos

produtos = ler_csv('vendas.csv')
produtos_entregue = filtrar_produtos_entregue(produtos)
valor_total_entregue = somar_valores_produtos(produtos_entregue)



pprint(produtos)
pprint(produtos_entregue)
print(valor_total_entregue)