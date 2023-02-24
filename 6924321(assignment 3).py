# a script on the prices of some cars at Cobra Dealership.
# Cobra Dealership is the right place to purchase your dream car.
# Cobra dealership deals in car brands like Nissan,Toyota,KiaHonda,and many others.
#prices of cars are in Ghana cedis.
Cars={
      'Kia rio':80000,'Kia optima':160000,'Kia picanto':65000,'Kia sportage':140000,'Suzuki alto':40000,
      'Toyota tundra':400000,'Toyota highlander':600000,'Toyota landcruiser':700000,'Toyota yaris':150000,'Toyota astra':195000,
      'Hyundai elantra':140000,'Hyundai accent':100000,'Hyundai sonata':170000,'Hyundai genesis':250000,
      'Hyundai Tucson':170000,'Hyundai i10':70000,
      'Honda crostour':350000, 'Honda accord':290000, 'Honda CR-V':340000,
      'Nissan almera':120000,'Nissan pathfinder':160000,'Nissan Xterra':100000,
      'Audi A5':185000,'Audi Q8':1280000,'Volvo sedans':542000,'Volvo S90':745000,'Volvo V60':590000,'Volvo suvs xc40':465000,
      'lexus':260000,'Ford':570000,
      }
car_name=input('Welcome to Cobra Dealership \
please specify car type: ') 
if car_name in Cars:
    print(f'the price of {car_name} is {Cars[car_name]:,} cedis ')
else:
    print(f'oops {car_name} is not available.Try other brands.eg:Nissan almera')  
    #https://github.com/users/Agbagah-7 