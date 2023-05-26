numum = int(input("Digite os gols do primeiro: "))
numdois = int(input("Digite os gols do segundo: "))

if numum == numdois:
    print("Empate")
elif numum < numdois:
    print("O segundo time ganhou")
else:
    print("O primeiro time ganhou")