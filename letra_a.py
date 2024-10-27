def contar_a(s):
    contador = 0
    for letra in s:
        if letra.lower() == 'a':
            contador += 1
    return contador

# Entrada do usuário
string = input("Informe uma string: ")
quantidade_a = contar_a(string)

print(f"A letra 'a' aparece {quantidade_a} vezes na string informada.")
