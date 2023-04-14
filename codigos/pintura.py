#! python


def retangulo(base, altura):
    area = base*altura
    return area


def tinta(area):
    vTinta = area*0.18
    return vTinta


def lTinta(vTinta):
    lTinta = vTinta/18
    return lTinta


if __name__ == '__main__':
    strBase = input('Insira a medida da Base: ')
    strAltura = input('Insira a medida da Altura: ')

    base = float(strBase)
    altura = float(strAltura)

    areaParede = retangulo(base, altura)
    string = 'A area da parede de base {}m e altura {}m e: {}m^2'
    print()
    print(string.format(base, altura, areaParede))
    print()

    lataTinta = tinta(retangulo(base, altura))
    volTinta = lTinta(tinta(retangulo(base, altura)))
    stringt = 'A quantidade de tinta utilizada' + \
        ' e {:.2f} latas, ou {:.2f} L de tinta'
    print()
    print(stringt.format(lataTinta, volTinta))
    print()
