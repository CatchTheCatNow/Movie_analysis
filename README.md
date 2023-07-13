# Movie analysis

- Step 1: **Read the data from the CSV file and create a dictionary for each movie, with the movie title as the key and the other data as values**
```- Import csv, copy and random modules
    - Create a values directory that has the year,     genre and rating keys with empty values
    - Include the movie_data.csv file to the program by using the 'with' statement 
    - Open the file using the 'open' function and the csv_file handle
    - Use the csv.reader() method to read the file
```
- Step 2: **Create a list of the movie dictionaries**
```- Create an empty list
    - Make a deep copy of the 'values' dictionary and add the data to it by iterating over the rows in the file and adding the values in it to the dictionary
    - Append the movie dictionaries to a list
```
- Step 3: **Calculate and print the number of movies in each genre, the average rating for each genre, and the number of movies released each year**
```- Create a function that calculates the amount of movies per year
    - Loop over the movies list and inside it create another for loop. Use the .items() method to iterate over each movie dictionary and calculate the required values. Use the function in the previous inside the loop. 
```
- Step 4: **Use the random module to select a random movie from the data and print the data for that movie**
```- Get a random movie using random.choise() and use it inside the loop
```
