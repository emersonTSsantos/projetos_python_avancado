# Uma função simples para dar exemplo para o generator
def my_gen():
    n = 1
    print('Primeiro print, n e igual a {}'.format(n))
    # A função geradora contém instruções yield
    yield n

    n += 1
    print('Segundo print, n e igual a {}'.format(n))
    yield n

    n += 1
    print('Terceiro e ultimo print , n e igual a {}'.format(n))
    yield n