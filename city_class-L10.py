class City:
    def __init__(self,city_name,region_name,country_name,population,zip_code,area_code):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.population = population
        self.zip_code = zip_code
        self.area_code = area_code

    def get_full_adress(self):
        return "{} {} ({}), {}.".format(self.city_name,self.zip_code,self.region_name,self.country_name)

petrzalka = City("Petržalka","Bratislavský Kraj","Slovensko",114000,"851 01","+421 2")
print(petrzalka.get_full_adress())

dnv = City("Devínska Nová Ves","Bratislavský Kraj","Slovensko",17067,"841 07","+421 2")
print(dnv.get_full_adress())