#Environmental impact fast vs sustainable fashion
#
#

import csv

"""CO2 emissions"""
#https://ccgga.org/cotton-information/much-cotton-take/
#--> 227g of cotton for 1 t-shirt and 680g for 1 pair of jeans
#
cotton_tshirt = 227
cotton_jeans = 680

#https://thepangaia.com/pages/discover-our-technologies
# --> 1 tonne of regular cotton fibre produces 1.8 tonnes of CO2
# --> 1g regular cotton produces 1.8g of CO2

rcotton_emissions = 1.80

#https://www.soilassociation.org/media/11662/coolcotton.pdf
# --> 978kg of CO2e per tonne of cotton fibre
# --> 1g organic cotton produces 0.98g CO2

scotton_emissions = 0.98

#CO2 emissions for regural cotton
emissions_rtshirt = cotton_tshirt * rcotton_emissions
emissions_rjeans = cotton_jeans * rcotton_emissions

#CO2 emissions for organic cotton
emissions_stshirt = cotton_tshirt * scotton_emissions
emissions_sjeans = cotton_jeans * scotton_emissions

#Percentage difference in CO2 emissions between regular and organic cotton

difference_tshirt = (round((emissions_stshirt - emissions_rtshirt)/ emissions_rtshirt, 2)) * 100
difference_jeans = (round((emissions_sjeans - emissions_rjeans)/ emissions_rjeans, 2)) * 100

print (difference_tshirt)
print (difference_jeans)

# --> Organic cotton produces approximately 46% less CO2 emissions

""" Water usage"""

#https://www.worldwildlife.org/stories/the-impact-of-a-cotton-t-shirt
# --> 2700L of water for 1 regular t-shirt
#https://www.un.org/actnow
# --> 10,000 litres of water are needed to make a single pair of jeans

water_rtshirt = 2700
water_rjeans = 10000

water_stshirt = 540
water_sjeans = 2000


with open('Environmental impact fast vs sustainable fashion.csv', 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['Type of clothing', 'CO2 emissions', 'Water usage', 'Percentage difference'])
    writer.writerow(['Fast fashion cotton t-shirt', emissions_rtshirt, water_rtshirt, 'N/A'])
    writer.writerow(['Sustainable cotton t-shirt', emissions_stshirt, water_stshirt, difference_tshirt])
    writer.writerow(['Fast fashion pair of jeans', emissions_rjeans, water_rjeans, 'N/A'])
    writer.writerow(['Sustainable pair of jeans', emissions_sjeans, water_sjeans, difference_jeans])






