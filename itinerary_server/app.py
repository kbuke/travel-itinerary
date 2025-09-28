from config import api, app

from resources.Country import CountriesList

from resources.Site import SitesList, Sites

from resources.Interests import InterestList

from resources.SiteInterests import SiteInterestsList

from resources.Cities import CityList, City

from resources.Users import UserList

from resources.SiteWishlist import SiteWishlistList

from resources.UserWishlists import UserWishlistList

api.add_resource(CountriesList, "/countries")

api.add_resource(SitesList, "/sites")
api.add_resource(Sites, "/sites/<int:id>")

api.add_resource(InterestList, "/interests")

api.add_resource(SiteInterestsList, "/siteinterests")

api.add_resource(CityList, "/cities")
api.add_resource(City, "/cities/<int:id>")

api.add_resource(UserList, "/users")

api.add_resource(UserWishlistList, "/wishlists")

api.add_resource(SiteWishlistList, "/sitewishlists")

if __name__ == "__main__":
    app.run(port=5555, debug=True)