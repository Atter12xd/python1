def maquina_de_turing(cadena):
    estado = 'q0'  # Estado inicial
    count_1s = 0   # Contador de 1s
    cinta = list(cadena)  # Convertir la cadena en lista
    i = 0  # Posición inicial del cabezal
    while i < len(cinta):
        simbolo = cinta[i]  # Leer el símbolo
        if estado == 'q0':  # Estado inicial
            if simbolo == '1':
                count_1s += 1  # Contar 1s
            i += 1  # Moverse a la derecha
    if count_1s % 2 == 0:
        return "La cadena tiene un número par de 1s."
    else:
        return "La cadena tiene un número impar de 1s."
# Ejemplo de uso
cadena = "01010101010101011"
resultado = maquina_de_turing(cadena)
print(resultado)