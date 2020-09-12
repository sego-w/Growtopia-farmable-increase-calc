# List of farmables and their respective increases/farm

# Edit: You can now select your own amount of seeds!

farmable = {'Rice':1.137,'Sugarcane':1.133,'Steel':1.107,'Ftank':1.096,'Pepper':1.090,'Chand':1.063,'Lgrid':1.072,'HTB':1.072,'Mbell':1.060,'Ladder':1.280,'Sorc':1.063,'Grass':1.990, 'Brick':1.971}

locals().update(farmable)

print("The following are valid entries to calculate: \n 'Rice' \n 'Sugarcane' \n 'Steel' \n 'Ftank' \n 'Pepper' \n 'Chand' \n 'Lgrid' \n 'HTB' \n 'Mbell' \n 'Ladder' \n 'Sorc' \n 'Grass' \n 'Brick'")

the_thing = input('Please enter the farmable you wish to calculate: ')

if the_thing not in farmable:
    print('Sorry, the farmable you entered is invalid.')
    exit()

amount = int(input('How many seeds are you starting with? '))

times = int(input('How many times are you planning to farm? '))

formula = amount * farmable[the_thing] ** times

print(f'By the time you finish farming, you should have {formula:.2f} Seeds!')

# this is a new comment