'''Dicionários ={} - Pode-se adicionar e retirar itens, valores.
    Para a criação de Dicionários, 
        a syntaxe utilizada será nomeDicionario {}'''

Numeros = {"Bruno": 10, "Renato": 8, "Paulo": 15}
print(Numeros)
Numeros["Cassio"] = 12
print(Numeros)
del Numeros["Bruno"]
print(Numeros)

'''Por tanto para eu adicionar um item ao meu dicionário, 
    devo inserir a syntaxe nomeDicionario["item"] = item
        enquanto para deletar, será utilizada a syntaxe del nomeDicionario ["item"]'''

contatos = {
    'Bruno_Siqueira': {
        'email': 'brunogsiq@gmail',
        'cel': '48 - 99105 - 9871'
    },
    'Bruno_Goncalves': {
        'email': 'brunosthill@gmail.com',
        'fone': 'Não Tem'
    }
}
print(contatos['Bruno_Siqueira']['email'])
print(contatos['Bruno_Goncalves']['fone'])
