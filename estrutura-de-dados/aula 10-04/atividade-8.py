def celsiusParaFahrenheit(temperaturaEmCelsius):
    temperaturaEmFahrenheit = (9*temperaturaEmCelsius + 160) / 5
    return temperaturaEmFahrenheit


def mostrarTemperatura(temperaturaCelsius, temperaturaFahrenheit):
    print(f"{temperaturaCelsius}ºC = {temperaturaFahrenheit}ºF")


def lerTemperatura():
    temperaturaCelsius = float(
        input('Digite a temperatura em ºC para converter para ºF: '))
    temperaturaFahrenheit = celsiusParaFahrenheit(temperaturaCelsius)
    mostrarTemperatura(temperaturaCelsius, temperaturaFahrenheit)


lerTemperatura()
