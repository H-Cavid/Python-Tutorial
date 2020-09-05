from lib import User
users=[]

def melumatlariAl():
    input_ad=input("Adinizi daxil edin:")
    input_soyad=input("Soyadinizi daxil edin:")
    input_username=input("Username-i daxil edin:")
    input_password=input("Parolunuzu daxil edin:")
    return[input_ad,input_soyad,input_username,input_password]

"""userMelumatlari=melumatlariAl()  --->>> silinsede proqram isdiyecek"""

"""for melumat in userMelumatlari:
   print(melumat)"""
"""user=User(userMelumatlari[0],userMelumatlari[1],userMelumatlari[2],userMelumatlari[3])---->===---->>>user=User(*userMelumatlari)"""
"""user=User(*melumatlariAl())
#built in function ---->>> users.append()
users.append()
user.showData(user) belede olar qisaltmaq ucun asagidaki kimi yazmaq meqsede uygundu"""

user=User(*melumatlariAl())
#built in function ---->>> users.append()
users.append(User(*melumatlariAl()))
users[0].showData()
def Qeydiyyat():
    userSayi=input("User sayini teyin edin:")
    for say in range(int(userSayi)):#int ona gore yaziriq ki range-in output-u reqemdi.
        users.append(User(*melumatlariAl()))
def MelumatlariGoster():
    for user in users:
        user.showData()
emr=input("Qeydiyyat prosesine baslamaq ucun 1 duymesine basin:")
if int(emr)==1:#int yazmaliyiqki bilsinki reqem daxil edecek,cunki inputun return-u stringdi.
    Qeydiyyat()
emr2=input("Butun emelliyatlari gormek ucun 2 duymesine basin")
if int(emr2)==2:
    MelumatlariGoster()

