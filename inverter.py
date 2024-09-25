

def inverter_string(texto):
    # Caso base: se a string estiver vazia ou com um caractere, retorna a própria string
    if len(texto) == 0:
        return texto
    else:
        # Chama a função novamente com a string sem o primeiro caractere, e adiciona o primeiro caractere ao final
        return inverter_string(texto[1:]) + texto[0]


texto = input("Digite uma string para inverter: ")
texto_invertido = inverter_string(texto)
print("String invertida:", texto_invertido)
