numero = "ab"

try:
    numero = int(numero)
except ValueError as e:
    print(f"O erro é o seguinte {e}")