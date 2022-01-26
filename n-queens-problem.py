from itertools import permutations
import numpy as np



def harita_ciz(cozum_matrisi, N):


    cozum_satir = []

    for i in cozum_matrisi:
        cozum_satir.append(i)

    cozum_sutun = []

    for i in range(N):
        cozum_sutun.append(i)

    konumlar = zip(cozum_satir,cozum_sutun)
    konumlar = tuple(konumlar)

    harita = np.zeros(shape=(N,N))

    for i in konumlar:

        x = i[0]
        y = i[1]

        harita[x][y] = 1


    return harita


###########################################################################

def main():

    bilgi = int(input("Örnek : ( 4 x 4 ) matris için '4' " 
                      "Matrisin boyutlarını giriniz : "))
    N = bilgi
    matris_boyutu = range(N)
    cozum = 0


    for kombinasyon in permutations(matris_boyutu):

        # sutunlar matrisi oluşturdur 0-1-2-3
        sutunlar = []
        for i in range(len(kombinasyon)):
            sutunlar.append(i)

        konumlar = zip(kombinasyon, sutunlar)
        konumlar = tuple(konumlar)
        eslesme_sayisi = 0

        for i in konumlar:  # 3. vezir
            for x in konumlar:  # 0 - 1 - 2 - 3

                x1 = i[0]
                y1 = i[1]

                x2 = x[0]
                y2 = x[1]

                if x1 == x2 and y1 == y2:
                    continue

                else:

                    if abs(x1 - x2) == abs(y1 - y2):
                        eslesme_sayisi += 1

                    else:
                        continue

        if eslesme_sayisi == 0:
            cozum += 1

            cozum_sutun = []

            for i in range(N):
                cozum_sutun.append(i)

            kombinasyon_degeri = zip(kombinasyon,cozum_sutun)
            kombinasyon_degeri = tuple(kombinasyon_degeri)

            print('\n\nÇözüm ' + str(cozum) + ': ' + str(kombinasyon_degeri) + '\n')

            print('\nÇözüm ' + str(cozum) + ' Harita : ' + '\n')

            print(harita_ciz(kombinasyon, N))

            print("\n\n_____________________________________________________")


        else:
            continue

    print("")
    print("Toplam oluşan çözüm matris sayısı : ",cozum)



###########

# çalıştır fonksiyonu

main()



