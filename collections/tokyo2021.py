import csv

countries = {}
sports = {}
counter = 0

# Open the data csv file
athletes_file = open('athletes.csv', 'r')
athletes_csv = csv.reader(athletes_file)

# for each line,
for line in athletes_csv:
    if counter == 0:
        counter += 1
        continue
    country = line[1]
    # if country in the dictionary, increase value by 1
    if country in countries:
        countries[country] += 1
    # else, add country in dictionary with a value of 1
    else:
        countries[country] = 1
    # do same with sport
    sport = line[2]
    if sport in sports:
        sports[sport] += 1
    else:
        sports[sport] = 1

# print the dictionary
print("COUNTRIES")
for key in countries:
    print(key, countries[key])
print("SPORTS")
for key in sports:
    print(key, sports[key])

# View countries in alphabetical order
print("COUNTRIES ORDERED BY NAME")
countries_list = sorted(countries.keys())
for key in countries_list:
    print(key, countries[key])

countries_values = countries.values()
print(countries_values)


