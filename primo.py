def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def siguiente_primo(numero):
    numero += 1
    while True:
        if es_primo(numero):
            return numero
        numero += 1

numero = int(input("Ingrese un número: "))

if es_primo(numero):
    print(numero, "es un número primo.")
else:
    siguiente = siguiente_primo(numero)
    print(f"{numero} no es primo. El siguiente número primo es {siguiente}.")