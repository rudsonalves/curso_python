# Modo Stream

try:
    file = open('pessoas.csv')
    firstLine = True

    for record in file:
        if firstLine:
            firstLine = False
            continue
        print('{} tem {} anos'.format(record.strip().split(',')))

finally:
    file.close()
    print('Fim!!!')
