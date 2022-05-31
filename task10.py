import re


def main(nbook):
    n2 = []
    for i in nbook:
        if i not in n2 and i[1] is not None:
            n2.append(i)
    n3 = []
    for i in range(0, len(n2)):
        stroka = n2[i][1].split('#')
        stroka1 = stroka[0]
        stroka3 = stroka[1]
        stroka1 = stroka1.replace('%', '')
        stroka1 = float(stroka1) / 100
        stroka1 = str(stroka1)
        if len(stroka1) == 3:
            stroka1 += '0'
        #
        stroka2 = n2[i][2].split('[at]')
        stroka2 = stroka2[0]
        #
        stroka3 = stroka3.replace('+7 ', '')
        stroka3 = stroka3.split('-')
        stroka3 = stroka3[-3] + '-' + stroka3[-2] + stroka3[-1]
        n3.append([stroka1, stroka2, stroka3])
    return n3


if name == 'main':
    nbook = [[None, '79%#+7 639 694-23-30', 'danila42[at]yandex.ru'],
             [None, '78%#+7 632 223-60-86', 'sizanic64[at]yandex.ru'],
             [None, None, None],
             [None, '10%#+7 917 503-12-53', 'cisisic79[at]yandex.ru']]

    print(main(nbook))
