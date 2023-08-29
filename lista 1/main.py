import data
import utils

# Testing add_person

utils.add_person(data.people_data, "Mike", 99, ["Soccer", "Ladies"])
utils.add_person(data.people_data, "Mike", 54, ["Dancing"])

print("\n")

utils.add_person(data.people_data, "Henzo", 144, ["Anime", "Cats"])

print("\n")

utils.add_person(data.people_data, "Saulo", 10, [])

print("\n")

for a in data.people_data:
    print(a)

print("\n")

# Testing remove_person

utils.remove_person(data.people_data, "Charlie")

for a in data.people_data:
    print(a)

print("\n")

# Testing get_ages

ages = utils.get_ages(data.people_data)

print(ages, end="\n\n")

# Testing get_hobbies

hobbies = utils.get_hobbies(data.people_data)

print(hobbies, end="\n\n")

# Testing get_people_by_hobbies

people = utils.get_people_by_hobbies(data.people_data, {"hobbies": "hiking"})

print(people, end="\n\n")

# Testing match_people

matched = utils.match_people(data=data.people_data, min_age=25,max_age=40)

print(matched, end="\n\n")

matched = utils.match_people(data=data.people_data)

print(matched, end="\n\n")

matched = utils.match_people(data=data.people_data, name="Henzo", min_age=25,max_age=40)

print(matched)

