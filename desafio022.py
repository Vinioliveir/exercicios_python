n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer \033[7m{}\033[m'.format(n))
print('Seu primeiro nome é \033[7m{}\033[m'.format(nome[0]))
print('Seu segundo nome é \033[7m{}\033[m'.format(nome[len(nome)-1]))