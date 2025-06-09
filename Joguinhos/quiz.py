print('=' * 40)
print('         QUIZ GEEK!         ')
print('  Teste seus conhecimentos e divirta-se!  ')
print('=' * 40)
print('\nVamos começar!\n')

pontuação = 0

print('=' * 40)
print('Quem foi a primeira protagonista feminina nos jogos?') 
print('1. Lara Croft em Tomb Raider') 
print('2. Ellie de The Last of Us parte 2') 
print('3. Jill Valentine em Resident Evil 3') 
print('4. Ms Pacman da franquia de Pacman') 
print('=' * 40)
resposta = int(input('Digite o número da resposta correta!^^ :'))
    
if resposta != 4:
    print('Opa! Resposta Errada... :( A resposta certa é...')
    print('Alternativa 4!^^')
else:
    print('Parabéns! Você Acertou e ganhou 1 ponto! ^^')
    pontuação += 1
    
print('=' * 40)
print('Quem desses NÃO foi um ator do Batman?') 
print('1. Ben Affleck') 
print('2. Daniel Craig') 
print('3. Michael Keaton') 
print('4. Gus Lewis') 
print('=' * 40)
resposta = int(input('Digite o número da resposta correta!^^ :'))
    
if resposta != 2:
    print('Opa! Resposta Errada... :( A respost certa é...')
    print()
    print('Alternativa 2!^^')
else:
    print('Parabéns! Você Acertou e ganhou 2 pontos! ^^')
    pontuação += 2

print('=' * 40)
print('Quem foi o primeiro campeão mundial de Pokemon World Championship?') 
print('1. Park Se-jun') 
print('2. Piter Bryon') 
print('3. Akira Toriyama') 
print('4. Yoo-Joonghyuk') 
print('=' * 40)
resposta = int(input('Digite o número da resposta correta!^^ :'))
    
if resposta != 1:
    print('Opa! Resposta Errada... :( A respost certa é...')
    print()
    print('Alternativa 1!^^')
else:
    print('Parabéns! Você Acertou e ganhou 3 pontos! ^^')
    pontuação += 3

print('=' * 40) 
print('Qual dessas afirmações sobre o personagem The Radiance é verdadeira?') 
print('1. The Radiance é a forma corrompida do Hollow Knight original.') 
print('2. The Radiance é uma entidade benevolente que guia os habitantes de Hallownest.') 
print('3. The Radiance é um ser de luz esquecido, responsável pela infecção mental dos insetos.') 
print('4. The Radiance era originalmente o pai do Hollow') 
print('=' * 40)
resposta = int(input('Digite o número da resposta correta!^^ :'))
    
if resposta != 3:
    print('Opa! Resposta Errada... :( A respost certa é...')
    print()
    print('Alternativa 3!^^')
else:
    print('Parabéns! Você Acertou e ganhou 2 pontos! ^^')
    pontuação += 2
    
print('=' * 40)
print('Black Dahlia é uma assasina cruel e boa de de briga. Qual é a arma mais icônica dela durante o combate?') 
print('1. Um chicote envenenado com veneno de Skullgirl') 
print('2. Lâminas ocultas nos braços') 
print('3. Um rifle-escopeta com munições especiais') 
print('4. Guarda-chuva que dispara ácido') 
print('=' * 40)
resposta = int(input('Digite o número da resposta correta!^^ :'))
    
if resposta != 3:
    print('Opa! Resposta Errada... :( A respost certa é...')
    print()
    print('Alternativa 3!^^')
else:
    print('Parabéns! Você Acertou e ganhou 1 ponto! ^^')
    pontuação += 1

print('=' * 40)
print('Qual anime NÃO foi clasificado como melhor anime do ano no Anime Awards 2025?') 
print('1. Dan Da Dan') 
print('2. Frieren e a Jornada para o além') 
print('3. Solo Levaling') 
print('4. Demon Slayer - Arco do Castelo Infinito') 
print('=' * 40)
resposta = int(input('Digite o número da resposta correta!^^ :'))
    
if resposta != 4:
    print('Opa! Resposta Errada... :( A respost certa é...')
    print()
    print('Alternativa 4!^^')
else:
    print('Parabéns! Você Acertou e ganhou 1 ponto! ^^')
    pontuação += 1

print('=' * 40)
print(f'Parabéns!^^ Você ficou com um total de {pontuação} pontos!ÒwÓ')
print('=' * 40)
