from flask import Flask
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Random joke from chuck norris: </strong>" + response['value']


@app.route('/category', methods=['GET'])
def get_chuck_norris_categories():
    api_url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(api_url).json()

    return "{}".format(response)


if __name__ == '__main__':
    app.run(debug=True)