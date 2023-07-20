from flask import Flask, jsonify
import requests
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

login_details = {
    "username": "password",
    "tejasree": "password"
}

@auth.verify_password
def verify(username, pwd):
    if not(username and pwd):
        return False
    return login_details.get(username) == pwd

url = "https://moviesminidatabase.p.rapidapi.com/movie/order/byPopularity/"

headers = {
	"X-RapidAPI-Key": "0c8e346fcbmshefe3d6c1f6bcfeap172f25jsn0f7979b8b900",
	"X-RapidAPI-Host": "moviesminidatabase.p.rapidapi.com"
}

@app.route("/movies")
@auth.login_required
def allmovies():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        movie_dict = response.json()
        return jsonify(movie_dict.get("results", []))
    else:
        return jsonify({"error": "Failed to fetch movies."}), 500

if __name__ == "__main__":
    app.run(debug=True)
