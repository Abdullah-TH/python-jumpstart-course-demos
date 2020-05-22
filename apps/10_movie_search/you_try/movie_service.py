import requests
import collections

Movie = collections.namedtuple("Movie",
                               "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")


def find_movies(search: str):
    if not search.strip():
        raise ValueError("Search text is required")

    url = f"http://movie_service.talkpython.fm/api/search/{search}"

    response = requests.get(url)
    response.raise_for_status()

    movies_data = response.json()
    hits_movies = movies_data["hits"]

    movies = [Movie(**movie_dict) for movie_dict in hits_movies]
    return movies
