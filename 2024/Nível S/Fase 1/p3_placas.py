placa = input()
if len(placa) == 8 and placa[3] == '-' and placa[:3].isalpha() and placa[4:].isnumeric():
    print(1)
elif len(placa) == 7 and placa[:3].isalpha() and placa[3].isnumeric() and placa[4].isalpha() and placa[5:].isnumeric():
    print(2)
else: print(0)