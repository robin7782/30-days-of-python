def countries_with_land(name):
    does_exist = 'land' in name
    if does_exist == True:
        return name        
land_countries = filter(countries_with_land, countries)
print(list(land_countries))