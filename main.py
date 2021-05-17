import csv
import operator

with open("MortalitateEU.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    args = {
        'codul': '',
        'tara': '',
        'Mortalitatea de la alcool': '',
        'Mortalitatea de la accidente': '',
        'Mortalitatea de la alte intimplari': '',
        'Mortalitatea de la stop cardiac': '',
        'Mortalitatea de la boli cronice': '',
        'Mortalitatea de la boli de ficat': '',
        'Mortalitatea de la Cancer': '',
        'Mortalitatea de la Diabet': '',
        'Mortalitatea de la Droguri': '',
        'Mortalitatea de la HIV': '',
        'Mortalitatea de la Omoruri': '',
        'Mortalitatea de la Pneumonie': '',
        'Mortalitatea de la Boli cu sistemul nervos': '',
        'Mortalitatea de la Sinucidere': ''
    }
    for row in file_reader:
        # print(f'{", ".join(row)}')
        args['codul'] = row[0]
        args['tara'] = row[1]
        args['Mortalitatea de la alcool'] = row[2]
        args['Mortalitatea de la accidente'] = row[3]
        args['Mortalitatea de la alte intimplari'] = row[4]
        args['Mortalitatea de la stop cardiac'] = row[5]
        args['Mortalitatea de la boli cronice'] = row[6]
        args['Mortalitatea de la boli de ficat'] = row[7]
        args['Mortalitatea de la Cancer'] = row[8]
        args['Mortalitatea de la Diabet'] = row[9]
        args['Mortalitatea de la Droguri'] = row[10]
        args['Mortalitatea de la HIV'] = row[11]
        args['Mortalitatea de la Omoruri'] = row[12]
        args['Mortalitatea de la Pneumonie'] = row[13]
        args['Mortalitatea de la Boli cu sistemul nervos'] = row[14]
        args['Mortalitatea de la Sinucidere'] = row[15]
        print('__________________________')
        print('Statistica pentru tara : ' + args['tara'])
        alc = args['Mortalitatea de la alcool']
        if not alc:
            print('*******************************************')
            print('nu are mortalitate din cauza alcoolului')
            print('*******************************************')
        else:
            print('mortalitatea de la alcool= ' + args['Mortalitatea de la alcool'])
        accid = args['Mortalitatea de la accidente']
        if not accid:
            print('*******************************************')
            print('nu are mortalitate din cauza accidentelor')
            print('*******************************************')
        else:
            print('mortalitatea de la accidente= ' + args['Mortalitatea de la accidente'])
        intimplari = args['Mortalitatea de la alte intimplari']
        if not intimplari:
            print('*******************************************')
            print('nu are mortalitate din cauza altor intimplari')
            print('*******************************************')
        else:
            print('mortalitatea de la alte intimplari= ' + args['Mortalitatea de la alte intimplari'])

        card = args['Mortalitatea de la stop cardiac']
        if not card:
            print('*******************************************')
            print('nu are mortalitate din cauza stopului cardiac')
            print('*******************************************')
        else:
            print('mortalitatea de la stop cardiac= ' + args['Mortalitatea de la stop cardiac'])
        cron = args['Mortalitatea de la boli cronice']
        if not cron:
            print('*******************************************')
            print('nu are mortalitate din cauza bolilor cronice')
            print('*******************************************')
        else:
            print('mortalitatea de la boli cronice= ' + args['Mortalitatea de la boli cronice'])
        ficat = args['Mortalitatea de la boli de ficat']
        if not ficat:
            print('*******************************************')
            print('nu are mortalitate din cauza bolilor de ficat')
            print('*******************************************')
        else:
            print('mortalitatea de la boli de ficat= ' + args['Mortalitatea de la boli de ficat'])
        cancer = args['Mortalitatea de la Cancer']
        if not cancer:
            print('*******************************************')
            print('nu are mortalitate din cauza bolilor de cancer')
            print('*******************************************')
        else:
            print('mortalitatea de la cancer= ' + args['Mortalitatea de la Cancer'])
        diabet = args['Mortalitatea de la Diabet']
        if not diabet:
            print('*******************************************')
            print('nu are mortalitate din cauza diabetului')
            print('*******************************************')
        else:
            print('mortalitatea de la diabet= ' + args['Mortalitatea de la Diabet'])
        drog = args['Mortalitatea de la Droguri']
        if not drog:
            print('*******************************************')
            print('nu are mortalitate din cauza drogurilor')
            print('*******************************************')
        else:
            print('mortalitatea de la droguri= ' + args['Mortalitatea de la Droguri'])
        hiv = args['Mortalitatea de la HIV']
        if not hiv:
            print('*******************************************')
            print('nu are mortalitate din cauza HIV')
            print('*******************************************')
        else:
            print('mortalitatea de la HIV= ' + args['Mortalitatea de la HIV'])
        omor = args['Mortalitatea de la Omoruri']
        if not omor:
            print('*******************************************')
            print('nu are mortalitate din cauza omorurilor')
            print('*******************************************')
        else:
            print('mortalitatea de la omor= ' + args['Mortalitatea de la Omoruri'])
        pneum = args['Mortalitatea de la Pneumonie']
        if not pneum:
            print('*******************************************')
            print('nu are mortalitate din cauza pneumoniei')
            print('*******************************************')
        else:
            print('mortalitatea de la pneumonie= ' + args['Mortalitatea de la Pneumonie'])
        sis_nerv = args['Mortalitatea de la Boli cu sistemul nervos']
        if not sis_nerv:
            print('*******************************************')
            print('nu are mortalitate din cauza bolilor cu sistemul nervos')
            print('*******************************************')
        else:
            print('mortalitatea de la bolile sistemului nervos= ' + args['Mortalitatea de la Boli cu sistemul nervos'])
        sinucidere = args['Mortalitatea de la Sinucidere']
        if not sinucidere:
            print('*******************************************')
            print('nu are mortalitate din cauza sinuciderilor')
            print('*******************************************')
        else:
            print('mortalitatea de la sinucideri= ' + args['Mortalitatea de la Sinucidere'])
