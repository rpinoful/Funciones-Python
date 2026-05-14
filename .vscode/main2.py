from pprint import pprint

from projeto import ler_csv_novo,processar_dados,calcular_vendas_categoria

produtos = ler_csv_novo('vendas2.csv')
produtos_entregue = processar_dados(produtos)
valor_total_entregue = calcular_vendas_categoria(produtos_entregue)



pprint(produtos)
pprint(produtos_entregue)
print(valor_total_entregue)