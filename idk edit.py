# List of farmables and their respective increases/farm

# Note: For this calculator, the assumed amount of seeds you have (one farm full) is 2496

farmable = {'Rice':1.137,'Sugarcane':1.133,'Steel':1.107,'Ftank':1.096,'Pepper':1.090,'Chand':1.063,'Lgrid':1.072,'HTB':1.072,'Mbell':1.060,'Ladder':1.280,'Sorc':1.063,'Grass':1.990}

locals().update(farmable)

print("The following are valid entries to calculate: \n 'Rice' \n 'Sugarcane' \n 'Steel' \n 'Ftank' \n 'Pepper' \n 'Chand' \n 'Lgrid' \n 'HTB' \n 'Mbell' \n 'Ladder' \n 'Sorc' \n 'Grass'")

the_thing = input('Please enter the farmable you wish to calculate: ')

if the_thing not in farmable:
    print('Sorry, the farmable you entered is invalid.')
    exit()

times = int(input('How many times are you planning to farm? '))

formula = 2496 * farmable[the_thing] ** times

print(f'By the time you finish farming, you should have {formula:.2f} Seeds!')

# thing