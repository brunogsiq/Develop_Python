''' Tuplas =() - Difere-se do Dicionário, 
        pois não é permitido adicionar nem remover valores.
    A syntaxe de criação das tuplas é nomeTupla= ("item1","item2","item3"). 
        Podemos descobrir as posições dos itens que estão
            presentes nesta Tupla, caso não possua um item, 
                será apresentado um erro, como no exemplo abaixo [3]'''

'''ListaNomes[3] print[3] - Exemplo de error'''

ListaNomes = ("Bruno", "Vampeta", "Ríncon")
ListaNomes2 = ("Ronaldo", "Marcelinho", "Ricardinho")
ListaNomes3 = ("Sport", "Clube", "Corinthians", "Paulista")
print(ListaNomes)

'''O comando len(), irá contar o número de variáveis ou strings dentro de uma tupla.'''

print(ListaNomes[0:3])
print(ListaNomes[0:2])
print(len(ListaNomes))

'''Pode-se realizar operações aritméticas com tuplas'''

ListaSoma = (ListaNomes + ListaNomes2 + ListaNomes3)
ListaMultiplica = (ListaNomes3 * 3)
print(ListaSoma)
print(ListaMultiplica)

'''Verificaçao de item em tupla'''

print("Parreira" in ListaSoma)
print("Bruno" in ListaSoma)

'''Pode-se converter Lista para Tuplas'''

ConverterListaParaTupla = [1, 4, "Item"]
print(ConverterListaParaTupla)
ConverterListaParaTupla2 = tuple(ConverterListaParaTupla)
print(ConverterListaParaTupla2)