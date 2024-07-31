# Função

def func_test(nome3, idade3):
    print("Meu nome é " + nome3)
    print("Tenho " + str(idade3) + " anos")

func_test("Bruno", 35)
func_test("Corinthians", 110)

def sumario():
    global NumeroSum
    NumeroSum = 1
    print("Inicial: " + str(NumeroSum))

sumario()
print(input("Final: " + str(NumeroSum)))