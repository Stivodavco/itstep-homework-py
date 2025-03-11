class Pasta:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self,ingredient):
        self.ingredients.append(ingredient)

    def show_ingredients(self):
        print("Ingredients:")
        index = 1
        for ingredient in self.ingredients:
            print(f"{index}. {ingredient}")
            index += 1

class PastaMaker:
    def __init__(self):
        self.pasta = Pasta()

    def add_type_of_pasta(self,type):
        self.pasta.add_ingredient(f"Pasta type: {type}")
        return self

    def add_sauce(self,sauce):
        self.pasta.add_ingredient(f"Sauce: {sauce}")
        return self

    def add_topping(self,topping):
        self.pasta.add_ingredient(f"Topping: {topping}")
        return self

    def add_dressing(self,dressing):
        self.pasta.add_ingredient(f"Dressing: {dressing}")
        return self

    def make_pasta(self):
        return self.pasta

pastaMaker = PastaMaker()
pasta = pastaMaker.add_type_of_pasta("Rigattoni").add_sauce("Tomato sauce").add_topping("Mashed tuna").add_dressing("Pasta dressing").make_pasta()
pasta.show_ingredients()