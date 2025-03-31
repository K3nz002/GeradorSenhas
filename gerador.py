import random
import string

def senha_facil():
    comprimento = 10
    caracteres = string.ascii_letters
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha

def senha_medio():
    comprimento = 16
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha

def senha_dificil():
    comprimento = 22
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha


nivel_senha = input('Escolha o nível de senha:\n1. Fácil\n2. Médio\n3. Difícil\n')

match nivel_senha:
    case '1':
        print('A senha gerada é:', senha_facil())
    case '2':
        print('A senha gerada é:', senha_medio())
    case '3':
        print('A senha gerada é:', senha_dificil())
