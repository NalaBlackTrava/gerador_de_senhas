import random # Módulo para geração de números aleatórios
import string # Módulo para manipulação de strings

def gerar_senha(tamanho=8):
    caracteres = string.hexdigits + string.punctuation                  # string.hexdigits = string.digits + string.ascii_letters
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))  # Gera uma senha aleatória usando os caracteres definidos
    return senha

print("Bem-vinde ao Gerador de Senhas da Na'linha terça-feira!")
comprimento = int(input("Digite o comprimento de senha que deseja: "))

senha_gerada = gerar_senha(comprimento)
print(f"Sua senha gereada é: {senha_gerada}")