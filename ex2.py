valor = float(input("Digite o valor: "))
num = float(input("Digite a quantidade de prestações: "))

prest = valor/num

if prest > 500:
    print("Usuário não consegue pagar")
else:
    print("Usuário consegue pagar")