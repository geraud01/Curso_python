# [expressão for item in list if condicional]
dobro_dos_pares = [i*2 for i in range(10) if i %2 == 0]
print(dobro_dos_pares)

#versão normal"
dobro_dos_pares =[]
for i in range(10):
    if i %2 == 0:
        dobro_dos_pares.append(i*2)
print(dobro_dos_pares)