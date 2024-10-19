class Restaurant:
    def __init__(self, name, location, cuisine_type, rating):
        self.name = name
        self.location = location
        self.cuisine_type = cuisine_type
        self.rating = rating

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Rating: {self.rating}")


class RestaurantManager:
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def display_all_restaurants(self):
        for restaurant in self.restaurants:
            restaurant.display_info()
            print("-" * 20)


if __name__ == "__main__":
    manager = RestaurantManager()

    # Example restaurants
    restaurant1 = Restaurant("Native Flavors", "New York, USA", "Native American", 4.5)
    restaurant2 = Restaurant("Earthly Delights", "Toronto, Canada", "Native American", 4.7)
    restaurant3 = Restaurant("Tribal Treats", "Sydney, Australia", "Native American", 4.6)

    manager.add_restaurant(restaurant1)
    manager.add_restaurant(restaurant2)
    manager.add_restaurant(restaurant3)

    manager.display_all_restaurants()
