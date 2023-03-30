import os
from flask import Flask
from StarWarsInfo import info_characters, info_movies



print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def list_movies():
    movies = info_movies()
    return(movies)

@app.route("/characters/<num>", methods=['GET'])
def list_characters(num: int):
    movies = info_characters(num)
    return(movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
