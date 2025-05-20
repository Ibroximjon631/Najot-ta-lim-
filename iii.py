class AbcKimdrla:
    kimdrla = {"Ali":["Ibroximov",1234567,123,5_000_000],
               "Ibroximjon":["Kimdr",123456789,12345,123_456]
               }
    def __init__(self,iii_l_name,iii_nmbr,pswd,karta_balans):
        self.iii_f_name:str
        self.iii_l_name = iii_l_name
        self.iii_nmbr = iii_nmbr
        self.pswd = int(pswd)
        self.karta_balans = karta_balans
        self.kartalar=[]
        self.karta = []


class Spr_Mrkt(AbcKimdrla):
    def __init__(self):
        self.iii_items = ""
        self.narx = 0
        self.iii = 1
        self.xyzi=False
        self.sprmarket_balans = 0
        self.__sprt_items={
            "Mandarin":[17000,"Kg",50],
            "Bread":[5000,"ta",77],
        }
    def kritish_info(self):
        self.iii_f_name = input("Name ni kiriting:").capitalize()
        if self.iii_f_name not in self.kimdrla:
            self.iii_l_name=input("Sz Royhatda yoqisiz.Fmla ni kiriting:").capitalize()
            self.iii_nmbr=input("Karta Nmbrni kiriting:")
            self.karta_balans=int(input("Karta balansini kiriting:(So'mda)"))
            self.pswd=input("Karta Pswd ni  kiriting:")


            AbcKimdrla.kimdrla[self.iii_f_name]=[self.iii_l_name,self.iii_nmbr,self.pswd,self.karta_balans]
    def Korsatish_items(self):
        iii=""
        i=1
        for name_ii, (narh,iiii,about) in self.__sprt_items.items():
            iii += f"{i}.Name:{name_ii}. Narhi: {narh},Bor:{about}{iiii}\n"
            i+=1
        return iii
    def by_item(self):
        while True:
            ii_item=int(input(f"--------------------------\nSpr Mrktda bor narsalar:\n{self.Korsatish_items()}\n--------------------------\n{self.iii_f_name}:) Nma kerak. Numberni kriting:"))
            if not self.__sprt_items:
                break
            else:
                abci=list(self.__sprt_items.keys())
                abcii=list(self.__sprt_items.values())
                item=int(input(f"Spr Mrktda {abci[ii_item-1]} {abcii[ii_item-1][2]}{abcii[ii_item-1][1]} bor.\nSzga neca {abcii[ii_item-1][1]} kerak?:"))
                while True:
                    if item>int(abcii[ii_item-1][2]) or item<0:
                        item=int(input(f"Notogri kirityapsiz. 1{abcii[ii_item-1][1] } dan {abcii[ii_item-1][2]}{abcii[ii_item-1][1] }gaca kiriting."))
                    else:
                        break
                self.iii_items+=f"{self.iii}.{item}{abcii[ii_item-1][1]} {abci[ii_item-1]}.\n"
                self.narx+=item*int(abcii[ii_item-1][0])
                self.__sprt_items[abci[ii_item-1]][2]-=item
                self.iii+=1
                if int(abcii[ii_item - 1][2]) == 0:
                    self.__sprt_items.pop(list(self.__sprt_items.keys())[ii_item - 1])
                ha_yoq=str(input("Szga boshqa nimadr kerakmi?(Ha/Yoq)").capitalize())
                if ha_yoq=="Ha":
                    continue
                else:
                    break
    def iii_narsalarini_korish(self):
        return (f"Szda bor mahsulotlar:\n{self.iii_items}Narsalar narhi:{self.narx}")


    def prcs_items(self):
        if self.narx<=int(self.kimdrla[self.iii_f_name][3]):
            self.sprmarket_balans+=self.narx
            self.kimdrla[self.iii_f_name][3]-=self.narx
            self.xyzi=True

        elif self.narx>int(self.kimdrla[self.iii_f_name][3]):
            ha_yq=input("Kartada balansi yetmiyapti.Ko'rasizmi/Kiritaszmi?:(Ha/Yoq)").capitalize()
            if ha_yq=="Ha":
                self.karta_balans_korish_qoshish()


    def karta_balans_korish_qoshish(self):
        iiii=int(input("--------------------------\nKatra balansini korish ucun 1 ni kriting.\nKarta balansi ni qo'shish ucun 2 ni kriting:"))
        if iiii==1:
            print(f"{self.kimdrla[self.iii_f_name][3]}so'm")
        elif iiii==2:
            prs=int(input("Kriting(So'mda):"))
            self.kimdrla[self.iii_f_name][3]+=prs



    def iiii(self):
        self.kritish_info()
        abci=False
        while True:
            xyz=int(input("--------------------------\n1.Mahsulotlarni ko'rish va Nimadr kerak bo'sa:)\n2.Narsalar szniki.\n3.Narsalarni Prs\n4.Karta balansi ko'rish va qo'shish\n5.Stp ucun.\nSz nimani bajarasiz.Nmbrni kriting:"))
            if xyz==1:
                self.by_item()
            elif xyz==2:
                print(self.iii_narsalarini_korish())
            elif xyz==3:
                self.prcs_items()
                if self.xyzi==True:
                    print("Rahmat")
                    break
            elif xyz==4:
                ixyziii = True
                while True:
                    if abci==False:
                        if ixyziii==False:
                            pswd=int(input("Pasword hato. Boshqa kiriting:"))
                            if pswd==int(self.kimdrla[self.iii_f_name][2]):
                                abci=True
                                self.karta_balans_korish_qoshish()
                                break
                        else:
                            pswd=int(input("Password ni kiriting:"))

                            if pswd==int(self.kimdrla[self.iii_f_name][2]):
                                abci=True
                                self.karta_balans_korish_qoshish()
                                break
                            else:
                                ixyziii=False
                    else:
                        self.karta_balans_korish_qoshish()
                        break

            elif xyz==5:
                print("Rahmat")
                break
if __name__=="__main__":
    ii=Spr_Mrkt()
    ii.iiii()
