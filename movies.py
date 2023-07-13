import csv
import copy
import random

values = {
    'year': 0,
    'genre': '',
    'rating': 0
}
dict_list = []

with open('movie_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for line in csv_reader:
        movie_values = copy.deepcopy(values)
        if line[0] == 'title':
            continue
        movie_values['year'] = line[1]
        movie_values['genre'] = line[2]
        movie_values['rating'] = line[3]
        dict_list.append({line[0]: movie_values}) 

def countMoviesPerYear(years, year):
    counted = 0
    length = len(years)
    for i in range(length):
        if years[i] == year:
            counted += 1
    return counted

movies_years = []
avg_rate_action = 0
count_action = 0
avg_rate_drama = 0
count_drama = 0
avg_rate_crime = 0
count_crime = 0

for item in dict_list:
    for key, value in item.items():
        random_dict = random.choice(dict_list)
        if value['genre'] == 'Action':
            avg_rate_action += float(value['rating'])
            count_action += 1
        elif value['genre'] == 'Drama':
            avg_rate_drama += float(value['rating'])
            count_drama += 1
        elif value['genre'] == 'Crime':
            avg_rate_crime += float(value['rating'])
            count_crime += 1
        movies_years.append(value['year'])
        if movies_years:
            print(f"The count of movies in year {value['year']} is {countMoviesPerYear(movies_years, value['year'])}")
        if random_dict and item == random_dict:
           print(f"The random movie is {key}, release year {value['year']}, genre {value['genre']}, rating {value['rating']}")

avg_rate_action = avg_rate_action / count_action  
avg_rate_drama = avg_rate_drama / count_drama
avg_rate_crime = avg_rate_crime / count_crime

print("Number of action movies:", count_action)
print("Number of dramas:", count_drama)
print("Number of crime movies:", count_crime)
print('The average rating per action movies is:', round(avg_rate_action, 2))
print('The average rating per drama movies is:', round(avg_rate_drama, 2))
print('The average rating per crime movies is:', round(avg_rate_crime, 2))



