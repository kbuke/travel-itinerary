from config import api, app

from resources.Country import CountriesList

from resources.Site import SitesList

from resources.Interests import InterestList

from resources.SiteInterests import SiteInterestsList

api.add_resource(CountriesList, "/countries")

api.add_resource(SitesList, "/sites")

api.add_resource(InterestList, "/interests")

api.add_resource(SiteInterestsList, "/siteinterests")

if __name__ == "__main__":
    app.run(port=5555, debug=True)