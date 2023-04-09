matriz = [[1, 2, 3], [4, 5, 6]]

linhasMatriz = len(matriz)
somaElementos = 0

for linha in range(linhasMatriz):
    colunasMatriz = len(matriz[linha])
    for coluna in range(colunasMatriz):
        somaElementos += matriz[linha][coluna]

print("Soma dos elementos da matriz: ", somaElementos)
