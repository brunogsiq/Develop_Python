# Pass # Break # Continue
NumeroTeste2 = 20
while True:
    NumeroTeste2 = NumeroTeste2 - 2
    print(NumeroTeste2)
    if(NumeroTeste2 < 2):
        break

NumeroTeste3 = 100
while True:
    NumeroTeste3 = NumeroTeste3 - 2
    if(NumeroTeste3 == 90):
        pass
    elif(NumeroTeste3 == 80):
        continue
    elif(print(NumeroTeste3 == 70)):
        pass
    else:
        break