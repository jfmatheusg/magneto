import numpy as np
import timeit

def checkDna(dnaStrip):
    mutantChains = ["AAAA","CCCC","GGGG","TTTT"]
    mutationsCount=0
    for mutantChain in mutantChains:
        if mutantChain in dnaStrip:
            mutationsCount+=dnaStrip.count(mutantChain)
            if mutationsCount>1:
                break

    return mutationsCount

def isMutant(dna):

    mutations = 0
    ticInit=timeit.default_timer()
    for dnaRow in dna:
        mutations+= checkDna(dnaRow)
        if mutations>1:
            print('1st loop time: ',(timeit.default_timer()-ticInit)*1000,'ms')
            print('Total time: ',(timeit.default_timer()-ticInit)*1000,'ms')
            return True
    print('1st loop time: ',(timeit.default_timer()-ticInit)*1000,'ms')

    tic=timeit.default_timer()
    dnaMatrix = np.array([list(row.encode()) for row in dna])
    print('Matrix generation: ',(timeit.default_timer()-tic)*1000,'ms')

    tic=timeit.default_timer()
    dnaMatrixT = dnaMatrix.T
    for column in dnaMatrixT:
        dnaColumn = bytes(column.tolist()).decode()
        mutations+= checkDna(dnaColumn)
        if mutations>1:
            print('2nd loop time: ',(timeit.default_timer()-tic)*1000,'ms')
            print('Total time: ',(timeit.default_timer()-ticInit)*1000,'ms')
            return True
    print('2nd loop time: ',(timeit.default_timer()-tic)*1000,'ms')

    tic=timeit.default_timer()
    dnaMatrixF = np.fliplr(dnaMatrix)
    lenRow=len(dna)
    for offset in range(-lenRow+4,lenRow-3):
        dnaDiagonal = bytes(np.diagonal(dnaMatrix,offset).tolist()).decode()
        dnaDiagonalF = bytes(np.diagonal(dnaMatrixF,offset).tolist()).decode()
        mutations+= checkDna(dnaDiagonal + " " + dnaDiagonalF)
        if mutations>1:
            print('3rd loop time: ',(timeit.default_timer()-tic)*1000,'ms')
            print('Total time: ',(timeit.default_timer()-ticInit)*1000,'ms')
            return True
    print('3rd loop time: ',(timeit.default_timer()-tic)*1000,'ms')
    print('Total time: ',(timeit.default_timer()-ticInit)*1000,'ms')
    return False

def dnaGenerator(size,noMutant=False):
    dna=[]
    dnaStrings=['A','C','G','T']
    if noMutant:
        dnaStrings=['Z','Y','X','W']
    for index in range(size):
        dna.append("".join([dnaStrings[np.random.randint(0,len(dnaStrings))] for i in range(size)]))
    return dna

mutantDna = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
normalDna = ["ATGCGA","CAGTGC","TTATTT","AGACGG","GCGTCA","TCACTG"]
print('isMutant?: ', isMutant(mutantDna))
print('isMutant?: ', isMutant(normalDna))

randomDna=dnaGenerator(100,True)
ticInit=timeit.default_timer()
print('isMutant? (dnaGenerator): ',isMutant(randomDna))
print('Total main time: ',(timeit.default_timer()-ticInit)*1000,'ms')
