import random
import string

def gerar_senha(tamanho=12, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    caracteres = ''
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso:
senha = gerar_senha(tamanho=16, maiusculas=True, minusculas=True, numeros=True, especiais=True)
print(senha)