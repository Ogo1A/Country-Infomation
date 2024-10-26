from countryinfo import CountryInfo
country = CountryInfo (input("Enter your country name:"))

print("Capital:",country.capital())
print("Population",country.population())
print("Area(in square kilometers):",country.area())
print("Region:",country.region())
print("Subregion:",country.subregion())
print("Demonym:",country.demonym())
print("Curreny:",country.currencies())
print("Languages:",country.languages())
print("Borders:",country.borders)