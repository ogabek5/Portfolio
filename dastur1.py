from datetime import datetime

def farq(yil):
    bugun=datetime.today()
    natija=bugun.year-int(yil)

    return natija 
tugilgan_yil=input("Tug'ilgan yilingizni kiriting \n>>>yilni kiriting: ")
natija_f=farq(tugilgan_yil) 

print(f'Natija: Siz {natija_f} yoshdasiz.')

maktab_yil=input("Maktabga kelgan yilingizni kiriting \n>>>yilni kiriting: ")
natija_f=farq(maktab_yil)
print(f"Natija: Maktabga kelganingizga {natija_f} yil bo'libdi.")














