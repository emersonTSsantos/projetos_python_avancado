import multiprocessing


# Criando uma variável global
results = []


def calc_square(numbers):
    global results
    for i in numbers:
        print('square: ', str(i*i))
        results.append(i*i)
        print('within a result: '+str(results))


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # criando um Processo aqui p1
    p1.start()
    # iniciando processos aqui em paralelo usando a função start.
    p1.join()
    # este join() aguardará até que a função calc_square() seja concluída.
    print('result : '+str(results))
    # Esta impressão não funcionou aqui, temos que imprimi-la dentro do processo
    print('Success')