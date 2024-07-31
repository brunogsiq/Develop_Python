'''Lista: Conjuntos de informações, que iniciam na posição Zero, 
    a syntaxe de criação é: nomeLista [ item1, item2, ...] '''

Listas =[]

Lista = [1, 4, 7, "Bruno", 10, 17]
print(Lista)

    # '''O comando .append adicionará o item que desejar a lista.'''
Lista.append("Siqueira")
Lista.append(23)
print(Lista)

'''O comando .index vai nos proporcionar saber a posição de um item dentro da nossa lista.'''
print(Lista.index(4))
print(Lista.index(17))
print(Lista.index("Bruno"))

'''O comando .count vai nos proporcionar saber a posição de um item dentro da nossa lista.'''
print(Lista.count(10))

'''Neste exemplo, adicionamos com o comando .append mais um número 10, 
    depois contamos quantas vezes ele está contido na lista.'''
Lista.append(10)
print(Lista)
print(Lista.count(10))

'''O comando .remove irá remover um item da lista que possa tornar-se desnecessário.'''
Lista.remove("Bruno")
print(Lista)

'''O comando .reverse() irá inverte a ordem dos itens na lista.'''
Lista.reverse()
print(Lista)

'''O comando .sort() irá ordenar numericamente ou por ordem alfabética a lista.'''
Lista2 = [10, 2, 8, 4, 6, 0]
Lista2.sort()
print(Lista2)
Lista3 = ['f', 'b', 'a', 'c', 'd']
Lista3.sort()
print(Lista3)

Lista4 = [1, 2, 17]
print(17 in Lista4.keys())
print(171 in Lista4.keys())