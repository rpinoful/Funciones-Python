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
# def filtrar_acima_limite(numeros :list[float], limite:float)  -> list : 
#     """
#     Filtra valores acima do limite 
#     Parametros : lista de numeros float , limite numerico
#     """
#     acima_limite =[num for num in numeros if num> limite]
    
    
    
#     return acima_limite


# print(filtrar_acima_limite([50,80,100,1000,347,200,10,20,30,90],99.9))



'''
3. Contar Valores Únicos em uma Lista
Crie uma função chamada contar_valores_unicos que receba uma lista de inteiros 
e retorne a quantidade de valores únicos presentes nessa lista como um int.
'''
#def valores_unicos_lista(numeros:list[int]) -> int:
    # lista_unica = []
    # contador = 0
    # for num in numeros:
    #     if num not in lista_unica:
    #         lista_unica.append(num)
    #         contador+=1
    
#     # outra forma 
#     numeros_set = set(numeros)
#     qtd_unicos= len(numeros_set)
            
            
#     return numeros_set,qtd_unicos

# numeros = [100,50,60,60,70,80,80,47,48,49,50,32,32,64,64,65,67,70,95]
# qtd_numeros,lista_numeros = valores_unicos_lista (numeros)
# print(qtd_numeros)
# print(lista_numeros)  





'''
4. Converter Celsius para Fahrenheit em uma Lista
Crie uma função chamada celsius_para_fahrenheit que receba uma lista de temperaturas em 
# Celsius do tipo float e retorne uma nova lista com todas as temperaturas convertidas para Fahrenheit.
# '''
# def convertir_celsius_farenheit(temperaturas:list[float]) -> list[float]:
#     """
#     Argumento : Lista de temperaturas do tipo float
#     Finalidade : Transforma temperaturas de unidades celsius para farenheit
#     Retorna : Lista de temperatura em formato farenheit
#     """
#     lista_formateada = [float(temp.replace("ºC","")) for temp in temperaturas ]
    
#     lista_farenheit =[round((temp*1.8)+32,2) for temp in lista_formateada]

#     return  lista_farenheit



# temperaturas_celsius = ["30.80ºC","100.05ºC","60.8ºC","75.8ºC","49.5ºC"]    
# temperaturas_farenheit = convertir_celsius_farenheit(temperaturas_celsius)
# print(temperaturas_farenheit)





'''
5. Calcular Desvio Padrão de uma Lista
Crie uma função chamada calcular_desvio_padrao que receba 
uma lista de números do tipo float e retorne o desvio padrão populacional desses valores como um float.

Formula = √(E(N-media)**2)/Quantidade de elementos

'''

# def desvio_padrao_lista(numeros:list[float]) -> float:
    
#     media = sum(numeros)/len(numeros)
    
    
#     desvio = sum((num - media)**2 for num in numeros)/len(numeros)
    
    
    
#     return desvio**0.5
    
    
    
    

# numeros = [10.5,14.8,30.9,40.4,90.5]
# desvio_padrao = desvio_padrao_lista(numeros)




'''
6. Encontrar Valores Ausentes em uma Sequência
Crie uma função chamada encontrar_valores_ausentes que receba uma lista de inteiros e retorne uma 
lista com todos os valores inteiros que estão faltando no intervalo entre o menor e o maior valor da lista.
'''
def encontrar_valores_ausentes(numeros:list[int]) -> list[int]:
    menor = min(numeros)
    maior = max(numeros)
    
    faltantes = []
    
    for i in range(menor+1,maior):
        faltantes.append(i)
        
    
    
    
    return faltantes
    
    
    
    

    
numeros = [100,50,60,60,70,80,80,47,48,49,50,32,32,64,64,65,67,70,95]
numeros_ausentes = encontrar_valores_ausentes(numeros)


