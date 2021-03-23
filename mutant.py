import numpy as np
import timeit

def checkDna(dnaStrip):
    mutantChains = ["AAAA","CCCC","GGGG","TTTT"]
    if any(mutantChain in dnaStrip for mutantChain in mutantChains):
            return 1
    return 0

def isMutant(dna):

    mutations = 0
    for dnaRow in dna:
        mutations+= checkDna(dnaRow)
        if mutations>1:
            return True

    dnaMatrix_ = []
    for row in dna:
        dnaMatrix_.append([ord(c) for c in row])
    else:
        lenRow=len(row)
    dnaMatrix = np.array(dnaMatrix_)
    dnaMatrixT = dnaMatrix.T

    for column in dnaMatrixT:
        dnaColumn = "".join([chr(value) for value in column.tolist()])
        mutations+= checkDna(dnaColumn)
        if mutations>1:
            return True

    dnaMatrixF = np.fliplr(dnaMatrix)
    for offset in range(-lenRow+4,lenRow-3):
        dnaDiagonal = "".join([chr(value) for value in np.diagonal(dnaMatrix,offset).tolist()])
        mutations+= checkDna(dnaDiagonal)
        if mutations>1:
            return True
        dnaDiagonalF = "".join([chr(value) for value in np.diagonal(dnaMatrixF,offset).tolist()])
        mutations+= checkDna(dnaDiagonalF)
        if mutations>1:
            return True
    return False

mutantDna = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
normalDna = ["ATGCGA","CAGTGC","TTATTT","AGACGG","GCGTCA","TCACTG"]
tic=timeit.default_timer()
print('mutant: ', isMutant(mutantDna))
toc=timeit.default_timer()
print('running time: ',toc-tic)
tic=timeit.default_timer()
print('mutant: ', isMutant(normalDna))
toc=timeit.default_timer()
print('running time: ',toc-tic)
