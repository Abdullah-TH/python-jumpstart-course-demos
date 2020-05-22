import movie_service
from requests.exceptions import ConnectionError


def main():
    print_header()


def print_header():
    print("-------------------------------------")
    print("        MOVIE SEARCH APP")
    print("-------------------------------------")


def search_event_loop():
    search = ""
    while search.lower() != "x":
        try:
            search = input("What movie do you want to search for [type x for exit]? ")
            movies = movie_service.find_movies(search)
            print(f"Found {len(movies)} movies for search {search}")
            for movie in movies:
                print(f"{movie.year} -- {movie.title}")
        except ValueError as error:
            print(error)
        except ConnectionError as error:
            print("Network is down, please connect to the internet")
        except Exception as error:
            print(f"Unexpected error: {error}")

    print("Exiting....")


if __name__ == '__main__':
    search_event_loop()
