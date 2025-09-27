from config import api, app

from resources.Country import CountriesList

api.add_resource(CountriesList, "/countries")

if __name__ == "__main__":
    app.run(port=5555, debug=True)