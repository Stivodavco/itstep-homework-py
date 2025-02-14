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

class Menu:
    @staticmethod
    def ukaz_menu(linked_list : LinkedList):
        print("(1) Add an item to the beginning of the list.")
        print("(2) Delete the last item from the list.")
        print("(3) Show the list contents")
        print("(4) Check if the list contains a value.")
        print("(5) Replace a value in the list at an index.")
        print("(6) Exit.")
        choice = input("Your choice (eg. \'1\'): ")

        if choice == "1":
            data = input("Data to insert: ")
            linked_list.vloz(data)
        elif choice == "2":
            linked_list.vymaz_posledny()
        elif choice == "3":
            linked_list.vypis()
        elif choice == "4":
            data = input("Data to find: ")
            linked_list.existuje_prvok(data)
        elif choice == "5":
            index = input("Index to replace: ")
            data = input("Data to replace it with: ")
            linked_list.nahrad_prvok(index,data)
        elif choice == "6":
            return
        else:
            print(f"\'{choice}\' is not a valid choice. Please enter 1,2,3,4,5 or 6.")

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