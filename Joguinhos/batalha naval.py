import random

print('=== BATALHA NAVAL ===')
print('Tente adivinhar onde está o navio! (entre 0 e 4)')

navio = random.randint(0, 4)
tentativas = 3

while tentativas > 0:
    chute = int(input('Escolha uma posição (0 a 4): '))

    if chute == navio:
        print('Você acertou o navio! Vitória!')
        break
    else:
        print('Errou! Tente de novo!^^')
        tentativas -= 1
        print('Tentativas restantes:', tentativas)

if tentativas == 0:
    print(f'Fim de jogo! O navio estava na posição {navio} OwO')
