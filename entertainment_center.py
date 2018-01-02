import fresh_tomatoes
import media

# The Avengers movie: title, poster and trailer
avengers = media.Movie(
    'The Avengers',
    'https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg', #NOQA
    'https://www.youtube.com/watch?v=eOrNdBpGMv8'
)

# Guardians of the Galaxy movie: title, poster and trailer
guardians_of_the_galaxy = media.Movie(
    'Guardians of the Galaxy',
    'https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg', #NOQA
    'https://www.youtube.com/watch?v=B16Bo47KS2g'
)

# John Wick: title, poster and trailer
john_wick = media.Movie(
    'John Wick: ', 
    'https://upload.wikimedia.org/wikipedia/en/thumb/9/98/John_Wick_TeaserPoster.jpg/220px-John_Wick_TeaserPoster.jpg', #NOQA
    'https://www.youtube.com/watch?v=RllJtOw0USI'
)

# Wonder Woman movie: title, poster and trailer
wonder_woman = media.Movie(
    'Wonder Woman',
    'https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg', #NOQA
    'https://www.youtube.com/watch?v=5lGoQhFb4NM'
)

# Death Note movie: title, poster and trailer
death_note = media.Movie(
    'Death Note', 
    'https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/DeathNotePoster.jpg/220px-DeathNotePoster.jpg', #NOQA
    'https://www.youtube.com/watch?v=R0BaQa0VNKk'
)

# Interstellar movie: title, poster and trailer
interstellar = media.Movie(
    'Interstellar',
    'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg', #NOQA
    'https://www.youtube.com/watch?v=zSWdZVtXT7E'
)

# Set the movies that will be passed to the media file
movies = [
    interstellar,
    john_wick,
    death_note,
    guardians_of_the_galaxy,
    avengers,
    wonder_woman
]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
