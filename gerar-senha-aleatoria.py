import random

print('Bem vindo(a) ao gerador de senhas aleatorias')

char = 'abcdefghijklmnopqrstuvwxyzçABCDEFGHJIJKLMNOPQRSTUVWXYZÇ!@$%^&*().,0123456789'

numero = input('Quantas senhas voce quer gerar? ')
numero = int(numero)

tamanho = input('Qual vai ser o tamanho da senha? ')
tamanho = int(tamanho)

print('\nEssas sao suas senhas: ')

for s in range(numero):
    senha = ''
    for c in range(tamanho):
        senha += random.choice(char)
    print(senha)