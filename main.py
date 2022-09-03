import random

vacation_locations = ["Miami", "Los Angeles", "New York City", "Houston", "Dubai", "Tokyo", "London", "Paris", "Rome"]
restaurants = ["Hard Rock Cafe", "Dorisa", "Nobu", "McDonald's", "Jack's Bistro", "Ray Brothers BBQ", "Nuovo Vesuvio"]
transportation_list = ["car", "boat", "plane", "jet ski", "bicycle"]
entertainment_list = ["a movie", "fishing", "sky diving", "scuba diving", "a comedy show"]
user_yes = "yes" or "Yes"
user_no = "no" or "No"
is_user_satisfied = "No"

def greeting():
    print("Welcome to your vacation day trip advisor! Below you will find a randomly selected location, restaurant, method of transportation, and form of entertainment for your day trip.")

def randomly_generated_location():
    selected_location = random.choice(vacation_locations)
    return selected_location

def randomly_generated_restaurant():
    selected_restaurant = random.choice(restaurants)
    return selected_restaurant

def randomly_generated_transportation():
    selected_transportation = random.choice(transportation_list)
    return selected_transportation

def randomly_generated_entertainment():
    selected_entertainment = random.choice(entertainment_list)
    return selected_entertainment

greeting()
selected_location = randomly_generated_location()
selected_restaurant = randomly_generated_restaurant()
selected_transportation = randomly_generated_transportation()
selected_entertainment = randomly_generated_entertainment()
