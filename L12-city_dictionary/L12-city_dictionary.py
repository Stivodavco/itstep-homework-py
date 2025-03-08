import pickle

def log(message):
    print("<Log>",message)

class Capitals:
    dictionary = {}

    @staticmethod
    def find_data(data):
        for country in Capitals.dictionary.keys():
            if country == data or Capitals.dictionary[country] == data:
                return country
        return None
    @staticmethod
    def add_data(country, capital):
        Capitals.dictionary.update({country:capital})
        log(f"Added data {country} : {capital}")

    @staticmethod
    def delete_data(data):
        Capitals.dictionary.pop(Capitals.find_data(data))
        log(f"Deleted data {data}")

    @staticmethod
    def edit_data(country,new_capital):
        found_country = Capitals.find_data(country)
        Capitals.dictionary[found_country] = new_capital
        log(f"Edited \'{country}\' capital to \'{new_capital}\'")

    @staticmethod
    def save_data(file = "dictionary.pickle"):
        with open(file,"wb") as fileHandler:
            pickle.dump(Capitals.dictionary,fileHandler)
            log(f"Saved dictionary to file {file}")

    @staticmethod
    def load_data(file = "dictionary.pickle"):
        with open(file,"rb") as fileHandler:
            loaded_dict = pickle.load(fileHandler)
            Capitals.dictionary = loaded_dict
            log(f"Loaded file {file}")

Capitals.load_data()
print(Capitals.dictionary)
Capitals.add_data("Hungary", "Budapest")
Capitals.delete_data("Hungary")
Capitals.add_data("Switzerland", "Berlin")
Capitals.edit_data("Switzerland","Bern")
Capitals.add_data("Poland", "Warsaw")
print(Capitals.find_data("Warsaw"))
# Capitals.save_data()