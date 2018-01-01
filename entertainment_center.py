import fresh_tomatoes
import media

avengers = media.Movie('The Avengers',
                    'https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg',
                    'https://www.youtube.com/watch?v=eOrNdBpGMv8')

guardians_of_the_galaxy = media.Movie('Guardians of the Galaxy',
                    'https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg',
                    'https://www.youtube.com/watch?v=B16Bo47KS2g')

john_wick = media.Movie('John Wick: ', 
                    'https://upload.wikimedia.org/wikipedia/en/thumb/9/98/John_Wick_TeaserPoster.jpg/220px-John_Wick_TeaserPoster.jpg',
                    'https://www.youtube.com/watch?v=RllJtOw0USI')

wonder_woman = media.Movie('Wonder Woman',
                    'https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg',
                    'https://www.youtube.com/watch?v=5lGoQhFb4NM')

death_note = media.Movie('Death Note', 
                    'https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/DeathNotePoster.jpg/220px-DeathNotePoster.jpg',
                    'https://www.youtube.com/watch?v=R0BaQa0VNKk')

interstellar = media.Movie('Interstellar',
                    'https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg',
                    'https://www.youtube.com/watch?v=zSWdZVtXT7E')

movies = [interstellar, john_wick, death_note, guardians_of_the_galaxy, avengers, wonder_woman]
fresh_tomatoes.open_movies_page(movies)