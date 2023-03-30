import requests 
from flask import jsonify


movie_url = "https://swapi.dev/api/films/"

def info_characters(num : int):
    data = requests.get(movie_url).json()
    movies=[]
    for movie in data["results"]:
        if int(movie["episode_id"]) == int(num):
            charactersURL= movie["characters"]
        
            characters=[]
        
            for url in charactersURL:
                data = requests.get(url).json()
                characters.append(data["name"])
            
            movies.append({
                "id": movie["episode_id"],
                "name": movie["title"],
                "characters" : characters
            })
    return jsonify(movies)

def info_movies():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    sorted_id = sorted(movies, key=lambda x: x["id"])
    
    
    return jsonify(sorted_id)