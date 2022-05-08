from sys import maxsize
number_of_movies = int(input())
highest_rating = -maxsize
lowest_rating = maxsize
average_rating = 0
highest_rated_movie = ''
lowest_rated_movie = ''
for watchlist in range(number_of_movies):
    name_of_movie = input()
    rating = float(input())
    if rating > highest_rating:
        highest_rating = rating
        highest_rated_movie = name_of_movie
    elif rating < lowest_rating:
        lowest_rating = rating
        lowest_rated_movie = name_of_movie
    average_rating += rating
    rating = 0
average_rating /= number_of_movies
print(f'{highest_rated_movie} is with highest rating: {highest_rating:.1f}')
print(f'{lowest_rated_movie} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')