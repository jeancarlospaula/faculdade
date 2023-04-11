def calculaDistanciaPercorridaViagem(duracao, velocidadeMedia):
    distanciaPercorrida = duracao * velocidadeMedia
    return distanciaPercorrida


def calculaQuantidadaLitrosCombustivelGastos(distancia):
    litrosGastos = distancia / 12
    return litrosGastos


def imprimeValores(velocidadeMedia, duracao, distanciaPercorrida, litrosGastos):
    print(f'Velodidade Média = {velocidadeMedia}km/h')
    print(f'Duração viagem = {duracao}h')
    print(f'Distancia percorrida = {distanciaPercorrida}km')
    print(f'Litros gastos = {litrosGastos}l')


def lerTempoVelocidadeViagem():
    velocidadeMedia = float(
        input('Digite a velocidade média da viagem (km/h): '))
    duracao = float(input('Digite a duração da viagem (h): '))
    distanciaPercorrida = calculaDistanciaPercorridaViagem(
        duracao, velocidadeMedia)
    litrosGastos = calculaQuantidadaLitrosCombustivelGastos(
        distanciaPercorrida)
    imprimeValores(velocidadeMedia, duracao, distanciaPercorrida, litrosGastos)


lerTempoVelocidadeViagem()
