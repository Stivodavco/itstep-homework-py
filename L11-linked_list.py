import warnings


class LinkedList: # custom version of a linked list (version developed in classroom)
    def __init__(self,head = None):
        self.head = head

    def ziskaj_posledny_prvok(self,prvok):
        if not prvok.dalsi_prvok:
            return prvok
        else:
            return self.ziskaj_posledny_prvok(prvok.dalsi_prvok)

    def vloz(self,prvok):
        if not self.head:
            self.head = prvok
        else:
            posledny_prvok = self.ziskaj_posledny_prvok(self.head)
            posledny_prvok.dalsi_prvok = prvok

    def vymaz_posledny(self):
        if not self.head:
            raise IndexError("List je prazdny!")
        else:
            aktualny = self.head
            while aktualny.dalsi_prvok.dalsi_prvok != None:
                aktualny = aktualny.dalsi_prvok
            aktualny.dalsi_prvok = None

    def existuje_prvok(self,data):
        aktualny = self.head
        while True:
            if aktualny.data == data:
                return True
            elif aktualny.dalsi_prvok is None:
                break
            else:
                aktualny = aktualny.dalsi_prvok
        return False

    def nahrad_prvok(self,index,nove_data):
        aktualny = self.head
        for i in range(index+1):
            if i == index:
                aktualny.data = nove_data
            elif aktualny.dalsi_prvok:
                aktualny = aktualny.dalsi_prvok
            else:
                raise IndexError("Zadany index je mimo rozsahu LinkedList!")

    def vypis(self):
        aktualny = self.head
        while True:
            print(aktualny.data)
            if not aktualny.dalsi_prvok:
                break
            aktualny = aktualny.dalsi_prvok

class Prvok:
    def __init__(self,data,dalsi_prvok = None):
        self.data = data
        self.dalsi_prvok = dalsi_prvok

# TEST
test = LinkedList()
test.vloz(Prvok("hello"))
test.vloz(Prvok(123))
test.vloz(Prvok(True))
test.vypis()
print("--------------")
test.vymaz_posledny()
test.vypis()
print("--------------")
test.nahrad_prvok(1,"woahhhh")
test.vypis()