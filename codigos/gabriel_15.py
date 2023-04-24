#! python

def horasAoMes(horas, dias):
    hAm = horas * dias * 4
    return hAm


def salBruto(ganhos, hAm):
    salB = ganhos*hAm
    return salB


def impostoRenda(salB):
    impRend = salB*0.11
    return impRend


def INSS(salB):
    inss = salB*0.08
    return inss


def sindicato(salB):
    sind = salB*0.05
    return sind


def salLiquido(salB, imRend, inss, sind):
    salL = salB-(imRend+inss+sind)
    return salL


if __name__ == '__main__':
    horas = float(input('Quantas horas voce trabalha por dia? '))
    dias = int(input('Quantos dias da semana voce trabalha? '))
    ganhos = float(input('Quanto voce ganha por hora? '))

    hAm = horasAoMes(horas, dias)
    salB = salBruto(ganhos, hAm)
    imRend = impostoRenda(salB)
    inss = INSS(salB)
    sind = sindicato(salB)
    salL = salLiquido(salB, imRend, inss, sind)

    strOut = '+ Salario Bruto: R$ {}, - Imposto de Renda: R$ {},' + \
        ' - INSS: R$ {}, - Sindicato: R$ {}, = Salario Liquido: R$ {}'
    print(strOut.format(salB, imRend, inss, sind, salL))
