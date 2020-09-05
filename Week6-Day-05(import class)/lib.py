#istifadeci class-i
#start of the class
class User :
    def __init__(self,_ad,_soyad,_username,_password):
        #atribute(statik xususiyyetleri yaziriq)
        self.ad=_ad
        self.soyad=_soyad
        self.username=_username
        self.password=_password

    def showData(self):#beheviour(methods)
        print(f"Melumatlariniz: {self.ad}, {self.soyad}, {self.username}, {self.password}")
 #end of the class