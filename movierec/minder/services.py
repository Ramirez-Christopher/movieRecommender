# Place your TMDB API utility function here, e.g., get_popular_movies(api_key)
import requests
def get_popular_movies(api_key):
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + api_key,    
        }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # This converts the JSON response to a Python dictionary
    else:
        return None
