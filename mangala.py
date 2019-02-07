kuyu = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]


def gorsel_yazdir():
    #     | 12 | 11 | 10 | 9  | 8  | 7  |
    #   x | x  | x  | x  | x  | x  | x  |
    #     | ----------------------------|
    #     | x  | x  | x  | x  | x  | x  | x
    #     | 1  | 2  | 3  | 4  | 5  | 6  |

    arr = []
    for x in kuyu:
        if x < 10:
            arr.append(str(x) + '  | ')
        else:
            arr.append(str(x) + ' | ')

    p1_arr = []
    for x in range(6):
        p1_arr.append(arr[x])

    p2_arr = []
    for x in range(12, 6, -1):
        p2_arr.append(arr[x])

    x = ' | '
    y = '| '

    print()
    print('  | 13 | 12 | 11 | 10 | 9  | 8  |')
    print('  | ----------------------------|')
    print('{0}{1}{2}'.format(str(kuyu[13]), (x if kuyu[13] <= 9 else y), ''.join(p2_arr)))
    print('  |                             |')
    print('  | ' + ''.join(p1_arr) + str(kuyu[6]))
    print('  | ----------------------------|')
    print('  | 1  | 2  | 3  | 4  | 5  | 6  |')
    print()


# hazinede toplam 48 taş olana kadar oyun devam edicek
while kuyu[6] + kuyu[13] != 48:
    gorsel_yazdir()
    konum = int(input('Hangi kuyudaki taşları almak istersin:')) - 1
    tassayisi = kuyu[konum]

    # oyuncu dağıtacığı kuyudaki taşların hepsini alır
    kuyu[konum] = 0

    # 14.kuyudan 1.kuyuya geçebilmek için kullandığımız formül
    for n in range(tassayisi):
        isaret = (konum + n) % 14

        # aldığımız taşların tek tek kuyuya atılması
        kuyu[isaret] = kuyu[isaret] + 1

        # taşı aldığımız konumda eğer 1 taş var ise sağa geçmesini sağlar
        if tassayisi == 1:
            kuyu[konum] = 0
            kuyu[konum + 1] = kuyu[konum + 1] + 1

    # eğer 1.oyuncu aldığı taşların sonuncusunu rakibin kuyusuna koyarsa
    #  ve kuyudaki taş sayısı çift sayı olursa ise bu taşları hazinesine ekler
    if konum >= 0 and konum <= 5 and isaret <= 12 and isaret >= 7 and kuyu[isaret] % 2 == 0:
        kuyu[6] = kuyu[6] + kuyu[isaret]
        kuyu[isaret] = 0
    elif konum >= 7 and konum <= 12 and isaret <= 5 and isaret >= 0 and kuyu[isaret] % 2 == 0:
        kuyu[13] = kuyu[13] + kuyu[isaret]
        kuyu[isaret] = 0

    # oyuncu taşları dağıtırken elinde kalan son taş yine kendi bölgesinde yer alan boş bir kuyuya denk gelirse ve eğer boş
    # kuyusunun karşısındaki kuyuda da rakibine ait taş varsa rakibinin kuyusundaki taşları alıp hazinesine katar
    if kuyu[isaret] == 1 and isaret != 6 and isaret != 13:
        if konum >= 0 and konum <= 5:
            geciciisaret = 0
            if isaret == 0:
                geciciisaret = 12
            elif isaret == 1:
                geciciisaret = 11
            elif isaret == 2:
                geciciisaret = 10
            elif isaret == 3:
                geciciisaret = 9
            elif isaret == 4:
                geciciisaret = 8
            elif isaret == 5:
                geciciisaret = 7
            kuyu[6] = kuyu[6] + kuyu[geciciisaret]
            kuyu[geciciisaret] = 0

        if konum >= 7 and konum <= 12:
            geciciisaret = 0
            if isaret == 12:
                geciciisaret = 0
            elif isaret == 11:
                geciciisaret = 1
            elif isaret == 10:
                geciciisaret = 2
            elif isaret == 9:
                geciciisaret = 3
            elif isaret == 8:
                geciciisaret = 4
            elif isaret == 7:
                geciciisaret = 5
            kuyu[13] = kuyu[13] + kuyu[geciciisaret]
            kuyu[geciciisaret] = 0
