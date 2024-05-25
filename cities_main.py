#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City

# Create a new state
state_1 = State(name="California")
state_1.save()
state_id_1 = state_1.id 
print("State ID 1:", state_1.id)  # Debug print

state_2 = State(name="Arizona")
state_2.save()
state_id_2 = state_2.id
print("State ID 2:", state_2.id)  # Debug print

city_1_1 = City(state_id=state_1.id, name="Napa")
city_1_1.save()
print("New city: {} in the state: {}".format(city_1_1, state_1))  # Existing print enhanced

city_1_2 = City(state_id=state_1.id, name="Sonoma")
city_1_2.save()
print("New city: {} in the state: {}".format(city_1_2, state_1))  # Existing print enhanced

city_2_1 = City(state_id=state_2.id, name="Page")
city_2_1.save()
print("New city: {} in the state: {}".format(city_2_1, state_2))  # Existing print enhanced
print("All states and their linked cities:")
linked_cities = []
all_states = storage.all(State)
for state_id, state in all_states.items():
    linked_cities = state.cities  # Assuming this is the getter you are using
    print(f"State: {state.name}, ID: {state.id}, Number of Cities: {len(linked_cities)}")
    for city in linked_cities:
        print(f"  City: {city.name}, City ID: {city.id}")
if len(linked_cities) != 2:
    print(f"FAIL: Expected 2 cities, found {len(linked_cities)} linked to State ID {state_id_1}")
    for city in linked_cities:
        print(f"  City ID: {city.id}, City Name: {city.name}, Linked State ID: {city.state_id}")
else:
    print("Success: Correct number of cities found linked to the state.")


