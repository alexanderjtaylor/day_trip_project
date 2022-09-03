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

while is_user_satisfied == "No":
    print(f"Location: {selected_location} - Restaurant: {selected_restaurant} - Transportation: {selected_transportation} - Enetertainment: {selected_entertainment}")
    user_satisfaction = input("Do you want to complete your day trip by confirming these selections?: ")
    if user_satisfaction == user_yes:
        print(f"Your plan is complete! You have selected a day trip in {selected_location} traveling by {selected_transportation} with {selected_entertainment} for your entertainment before your dinner at {selected_restaurant}. Have fun!")
        is_user_satisfied = "Yes"
    elif user_satisfaction == user_no:
        change_location = input("Do you want to change the location of your trip?: ")
        if change_location == user_yes:
            vacation_locations.remove(selected_location)
            selected_location = random.choice(vacation_locations)
        elif change_location == user_no:
            change_restaurant = input("Do you want to change the restaurant for your trip?: ")
            if change_restaurant == user_yes:
                restaurants.remove(selected_restaurant)
                selected_restaurant = random.choice(restaurants)
            elif change_restaurant == user_no:
                change_transportation = input("Do you want to change your method of transportation?: ")
                if change_transportation == user_yes:
                    transportation_list.remove(selected_transportation)
                    selected_transportation = random.choice(transportation_list)
                elif change_transportation == user_no:
                    change_entertainment = input("Do you want to change your entertainment for the trip?: ")
                    if change_entertainment == user_yes:
                        entertainment_list.remove(selected_entertainment)
                        selected_entertainment = random.choice(entertainment_list)
                    elif change_entertainment == user_no:
                        print("No other selections left to change. Check selections again")
                    else:
                        print("Invalid entry, try agin...")
                else:
                    print("Invalid entry, try agin...")
            else:
                print("Invalid entry, try agin...")
        else:
            print("Invalid entry, try agin...")
    else:
        print("Invalid entry, try agin...")