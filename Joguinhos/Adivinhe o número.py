import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print('Olá! ^.^ Vamos jogar um jogo de adivinhação!')
    print('Estou pensando em um número entre 1 e 100. Tente adivinhar qual é! ;D')

    while not acertou:
        try:
            resposta = int(input('Escreva um número^^ : '))
            tentativas += 1

            if resposta < numero_secreto:
                print('Resposta muito baixa... Próxima dica :3 :')
                print('O número é maior que esse ^^')
            elif resposta > numero_secreto:
                print('Resposta muito alta... Próxima dica :3 :')
                print('O número é menor que esse ^^')
            else:
                acertou = True
                print(f'Wow que sorte! Você acertou em {tentativas} tentativas! ÒwÓ ')
                
        except ValueError:
            print('Opa! Parece que você não digitou um número válido. Tente de novo! >w<')

    print('\nParabéns! Você conseguiu achar o número secreto!!ÒwÓ')
    print('Obrigado por jogar! <3')

if __name__ == "__main__":
    jogar()