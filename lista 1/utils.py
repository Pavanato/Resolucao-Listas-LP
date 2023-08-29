def add_person(data, name, age, hobbies):
    # Check repetition
    for index in data:
        if name.upper() in index["name"].upper():
            print("This name has already been taken")
            return data

    try:
        if 0 >= age or age >= 100:
            raise ValueError
        if not bool(hobbies):
            raise
    except ValueError:
        print("Age should be between 0 and 100 years")
        return data
    except:
        print("Insert at least 1 hobbie")
        return data
    
    data.append({"name": name, "age": age, "city": "", "hobbies": hobbies})
    return data

def remove_person(data, name):
    for index in data:
        if name.upper() in index["name"].upper():
            data.remove(index)
            return data

    print(f"{name} is not in the data")
    return data
        
def get_ages(data):
    ages = []   
    for index in data:
        ages.append(index["age"])
    
    return (min(ages), int(sum(ages) / len(ages)), max(ages))

def get_hobbies(data):
    dic = {}
    for i, index in enumerate(data):
        dic[index["name"]] = index["hobbies"]
    return dic

def get_people_by_hobbies(data: list, hobbies: dict):
    sorted_data = sorted(data, key=lambda x: x['age'])
    names = []
    for index in sorted_data:
        for values in hobbies.values():
            if values in index['hobbies']:
                names.append(index['name'])
    return names
    

def match_people(data, name=None, min_age=None, max_age=None, city=None, hobbies=[]):
    sorted_data = sorted(data, key=lambda x: x['age'])
    names = []
    
    # Limitation to min and max age by default
    if min_age == None:
        min_age = 0
    if max_age == None:
        max_age = 100

    try:
        if min_age > max_age:
            raise ValueError
    except ValueError:
        print("max_age should be greater than min_age")
        return names

    for index in sorted_data:
        # Create temporary variables
        if name == None:
            cur_name = index["name"]
        else:
            cur_name = name
        if city == None:
            cur_city = index["city"]
        else:
            cur_city = city
        if hobbies == []:
            cur_hobbies = index["hobbies"]
        else:
            cur_hobbies = hobbies

        # Tests restrictions
        if cur_name != index["name"] or min_age >= index["age"] or max_age <= index["age"] or cur_city != index["city"] or sorted(cur_hobbies) != sorted(index["hobbies"]):
            cur_name = None
            cur_city = None
            cur_hobbies = []
            continue
        else:
            names.append(index["name"])
    return names