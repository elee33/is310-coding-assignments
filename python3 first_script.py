# Define your list of favorite movies
favorite_movies = [
    {
        "name": "The Matrix",
        "release_year": 1999,
        "sequels": ["The Matrix Reloaded", "The Matrix Revolutions"]
    },
    {
        "name": "Inception",
        "release_year": 2010,
        "sequels": []
    },
    {
        "name": "Toy Story",
        "release_year": 1995,
        "sequels": ["Toy Story 2", "Toy Story 3", "Toy Story 4"]
    }
]

# Define the function to check movie release year
def check_movie_release(movie):
    if movie['release_year'] < 2000:
        print("This movie was released before 2000")
    else:
        print("This movie was released after 2000")
        return movie['name']

# Create an empty list to store recent movies
recent_movies = []

# Loop through your favorite movies
for movie in favorite_movies:
    result = check_movie_release(movie)
    if result is not None:
        recent_movies.append(movie)

# Print out the recent movies list
print("Recent movies released after 2000:")
print(recent_movies)




