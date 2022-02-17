# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_damages(dmg_lst):
  updated_damages = []
  for val in dmg_lst:
    if val == "Damages not recorded":
      updated_damages.append(val)
    else:
      updated_damages.append(float(val[:-1])*conversion[val[-1]]) 
  return updated_damages

# test function by updating damages
updated_damages = update_damages(damages)
print(updated_damages)
print('\n\n')
# 2 
# Create a Table
def make_dict(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths):
  table = {}
  for i in range(0,len(names)):
    table[names[i]] = {'Name':names[i], 'Month': months[i], 'Year': years[i], 'Max sustained wind': max_sustained_winds[i], 'Areas': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
  return table

# Create and view the hurricanes dictionary
hurricane_dict = make_dict(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)
print(hurricane_dict)
print('\n\n')

# 3
# Organizing by Year
def organize_by_years(hurricane_dict):
  new_hurricane_dict = {}
  for hurricane in hurricane_dict:
    current_year = hurricane_dict[hurricane]['Year']
    current_cane = hurricane_dict[hurricane]
    if current_year in new_hurricane_dict:
      new_hurricane_dict[current_year].append(current_cane)
    else: 
      new_hurricane_dict[current_year] = [current_cane]
  return new_hurricane_dict
# create a new dictionary of hurricanes with year and key
print('\n\n')
print(organize_by_years(hurricane_dict))

# 4
# Counting Damaged Areas
def count_areas(hurricane_dict):
  areas_dict = {}
  for hurricane in hurricane_dict:
    for area in hurricane_dict[hurricane]['Areas']:
      if area in areas_dict:
        areas_dict[area] += 1
      else: areas_dict[area] = 1
  return areas_dict


# create dictionary of areas to store the number of hurricanes involved in
print('\n\n')
print(count_areas(hurricane_dict))

# 5 
# Calculating Maximum Hurricane Count
def find_area(areas_dict):
  max_area = {'Initial':0}
  for area in areas_dict:
    if areas_dict[area] > list(max_area.values())[0]:
      max_area = {area: areas_dict[area]}
    return max_area

# find most frequently affected area and the number of hurricanes involved in
print('\n\n')
print(find_area(count_areas(hurricane_dict)))

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricane_dict):
  max_deaths = {'Initial':0}
  for hurricane in hurricane_dict:
    if hurricane_dict[hurricane]['Deaths'] > list(max_deaths.values())[0]:
      max_deaths = {hurricane: hurricane_dict[hurricane]['Deaths']}
  return max_deaths

# find highest mortality hurricane and the number of deaths
print('\n\n')
print(deadliest_hurricane(hurricane_dict))

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def rate_hurricane(hurricanes_dict):
  mortality_ratings = {0: [], 1:[], 2:[], 3: [], 4:[]}
  for hurricane in hurricanes_dict:
    if hurricanes_dict[hurricane]['Deaths'] == mortality_scale[0]:
      mortality_ratings[0].append(hurricane)
    elif hurricanes_dict[hurricane]['Deaths'] <= mortality_scale[1]:
      mortality_ratings[1].append({hurricane: hurricanes_dict[hurricane]['Deaths']})
    elif hurricanes_dict[hurricane]['Deaths'] <= mortality_scale[2]:
      mortality_ratings[2].append({hurricane: hurricanes_dict[hurricane]['Deaths']})
    elif hurricanes_dict[hurricane]['Deaths'] <= mortality_scale[3]:
      mortality_ratings[3].append({hurricane: hurricanes_dict[hurricane]['Deaths']})
    else:
      mortality_ratings[4].append({hurricane: hurricanes_dict[hurricane]['Deaths']})
  return mortality_ratings
# categorize hurricanes in new dictionary with mortality severity as key

print('\n\n')
print(rate_hurricane(hurricane_dict))


# 8 Calculating Hurricane Maximum Damage
def greatest_damage(hurricane_dict):
  max_damage = {'Initial':0}
  for hurricane in hurricane_dict:
    if hurricane_dict[hurricane]['Damage'] == 'Damages not recorded':
      continue
    else:
      if hurricane_dict[hurricane]['Damage'] > list(max_damage.values())[0]:
        max_damage = {hurricane: hurricane_dict[hurricane]['Damage']}
  return max_damage
  
# find highest damage inducing hurricane and its total cost
print('\n\n')
print(greatest_damage(hurricane_dict))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def rate_damage(hurricanes_dict):
  damage_ratings = {0: [], 1:[], 2:[], 3: [], 4:[], 5:[]}
  for hurricane in hurricanes_dict:
      current_damage = hurricanes_dict[hurricane]['Damage']
      if current_damage == 'Damages not recorded':
        damage_ratings[0].append({hurricane: current_damage})
      elif current_damage <= damage_scale[1]:
        damage_ratings[1].append({hurricane: current_damage})
      elif current_damage <= damage_scale[2]:
        damage_ratings[2].append({hurricane: current_damage})
      elif current_damage <= damage_scale[3]:
        damage_ratings[3].append({hurricane: current_damage})
      elif current_damage <= damage_scale[4]:
        damage_ratings[4].append({hurricane: current_damage})
      else:
        damage_ratings[5].append({hurricane: current_damage})
  return damage_ratings  
# categorize hurricanes in new dictionary with damage severity as key
print('\n\n')
print(rate_damage(hurricane_dict))