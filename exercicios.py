'''
1. Calcular Média de Valores em uma Lista

Crie uma função chamada calcular_media que receba uma lista de números do tipo float
 
e retorne a média aritmética desses valores como um float.
'''

# def func_media(numeros :list[float])->float:
#     soma_valores = sum(numeros)
#     qtd_numeros = len(numeros)   
#     return (soma_valores/qtd_numeros)


# numeros = [1.4,2.8,3.5,4.7,5.1,6.3,7.4]
# media = func_media(numeros)
# print(media)



'''
2. Filtrar Dados Acima de um Limite
Crie uma função chamada filtrar_acima_de que receba uma lista de números do tipo float e um valor limite também float,
e retorne uma nova lista contendo apenas os valores maiores que o limite.
'''
def filtrar_acima_limite(numeros :list[float], limite:float)  -> list : 
    """
    Filtra valores acima do limite 
    Parametros : lista de numeros float , limite numerico
    """
    acima_limite =[num for num in numeros if num> limite]
    
    
    
    return acima_limite






print(filtrar_acima_limite([50,80,100,1000,347,200,10,20,30,90],99.9))
