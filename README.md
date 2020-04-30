# Growtopia-farmable-increase-calc
This is a fun little tool I built to help growtopians quickly calculate their wanted amount of seeds after a farming session!

# List of farmables and their respective increases/farm

# Note: For this calculator, the assumed amount of seeds you have (one farm full) is 2496
```
farmable = {'Rice':1.137,'Sugarcane':1.133,'Steel':1.107,'Ftank':1.096,'Pepper':1.090,'Chand':1.063,'Lgrid':1.072,'HTB':1.072,'Mbell':1.060,'Ladder':1.280,'Sorc':1.063,'Grass':1.990}
locals().update(farmable)

print("The following are valid entries to calculate: \n 'Rice' \n 'Sugarcane' \n 'Steel' \n 'Ftank' \n 'Pepper' \n 'Chand' \n 'Lgrid' \n 'HTB' \n 'Mbell' \n 'Ladder' \n 'Sorc' \n 'Grass'")
the_thing = input('Please enter the farmable you wish to calculate: ')
times = int(input('How many times are you planning to farm? '))
formula = 2496 * farmable[the_thing] ** times

if the_thing == 'Rice':
	formula = 2496 * farmable['Rice'] ** times
elif the_thing == 'Sugarcane':
	formula = 2496 * farmable['Sugarcane'] ** times
elif the_thing == 'Steel':
	formula = 2496 * farmable['Steel'] ** times	
elif the_thing == 'Ftank':
	formula = 2496 * farmable['Ftank'] ** times
elif the_thing == 'Pepper':
	formula = 2496 * farmable['Pepper'] ** times
elif the_thing == 'Chand':
	formula = 2496 * farmable['Chand'] ** times
elif the_thing == 'Lgrid':
	formula = 2496 * farmable['Lgrid'] ** times
elif the_thing == 'HTB':
	formula = 2496 * farmable['HTB'] ** times
elif the_thing == 'Mbell':
	formula = 2496 * farmable['Mbell'] ** times
elif the_thing == 'Ladder':
	formula = 2496 * farmable['Ladder'] ** times
elif the_thing == 'Sorc':
	formula = 2496 * farmable['Sorc'] ** times
elif the_thing == 'Grass':
	formula = 2496 * farmable['Grass'] ** times
else:
	print('Sorry, the farmable you entered is invalid.')




print(f'By the time you finish farming, you should have {formula:.2f} Seeds!')
```
