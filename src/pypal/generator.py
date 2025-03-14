"""
This module provides a function to retrieve a pseudo-random line from Lewis Carroll's poem "The Jabberwocky".
Read more about Jabberwocky here: https://en.wikipedia.org/wiki/Jabberwocky
"""
import random

# names.py
def generate_name(type="human", length=2):
    human_first = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Julia"]
    human_last = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Clark", "Lewis", "Walker", "Young", "Hall"]
    fantasy_names = ["Zorblax", "Elandra", "Thrain", "Myrrha", "Drakar", "Lyssara", "Volgrim", "Zenthra", "Kaelith", "Orvax"]

    result = []
    for _ in range(length):
        if type == "human":
            name = f"{random.choice(human_first)} {random.choice(human_last)}"
        elif type == "fantasy":
            name = random.choice(fantasy_names)
        else:
            raise ValueError("Invalid type. Choose 'human' or 'fantasy'.")
        result.append(name)
    return result

# addresses.py
def generate_address(country="US", format="short"):
    streets = ["123 Maple St", "456 Oak Ave", "789 Pine Rd", "101 Elm St", "202 Birch Blvd", "303 Cedar Ln", "404 Spruce Ct", "505 Walnut Way"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
    postcodes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101"]
    uk_postcodes = ["EC1A 1BB", "W1A 0AX", "M1 1AE", "B33 8TH", "CR2 6XH", "DN55 1PT", "E1 6AN", "N1 9GU"]

    street = random.choice(streets)
    city = random.choice(cities)

    if country == "US":
        if format == "short":
            return f"{street}, {city}"
        elif format == "long":
            return f"{street}, {city}, {random.choice(postcodes)}, USA"
    elif country == "UK":
        if format == "short":
            return f"{street}, {city}"
        elif format == "long":
            return f"{street}, {city}, {random.choice(uk_postcodes)}, UK"
    else:
        raise ValueError("Invalid country. Choose 'US' or 'UK'.")

# phone_numbers.py
def generate_phone_number(style="domestic"):
    area_code = random.randint(100, 999)
    prefix = random.randint(100, 999)
    line = random.randint(1000, 9999)

    if style == "domestic":
        return f"({area_code}) {prefix}-{line}"
    elif style == "international":
        return f"+1-{area_code}-{prefix}-{line}"
    else:
        raise ValueError("Invalid style. Choose 'domestic' or 'international'.")


