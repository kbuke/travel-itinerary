from config import api, app

from resources.Country import CountriesList

from resources.Site import SitesList

api.add_resource(CountriesList, "/countries")

api.add_resource(SitesList, "/sites")

if __name__ == "__main__":
    app.run(port=5555, debug=True)