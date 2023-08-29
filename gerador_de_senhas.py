import random
import string

# Função para gerar a senha
def gerar_senha(tamanho=8, letras_repetidas=False, caracteres_especiais=False):
    caracteres = string.hexdigits  # hexdigits inclui dígitos e letras em maiúsculas e minúsculas
    if caracteres_especiais:
        caracteres += string.punctuation  # Adiciona caracteres especiais se desejado
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    if not letras_repetidas:
        senha = ''.join(random.sample(senha, len(senha)))  # Embaralha a senha para evitar letras repetidas
    return senha

# Loop principal
while True:
    print("Bem-vinde ao Gerador de Senhas da Na'linha terça-feira! :) \n")

    comprimento = int(input("Digite o comprimento de senha que deseja: "))
    letras_repetidas = input("Deseja permitir letras repetidas? (s/n): ").lower() == "s"
    caracteres_especiais = input("Deseja incluir caracteres especiais? (s/n): ").lower() == "s"

    senha_gerada = gerar_senha(comprimento, letras_repetidas, caracteres_especiais)
    print(f"Sua senha gerada é: {senha_gerada}")

    continuar = input("Deseja gerar outra senha? (s/n): ").lower()
    if continuar != "s":
        print("Obrigada por usar meu Gerador de Senhas!  Até a próxima ✿ ◕ ‿ ◕ ✿")
        break  # Sai do loop ao escolher "n"