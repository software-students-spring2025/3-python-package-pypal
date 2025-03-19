import pytest
from pypal.generator import generate_name, generate_address, generate_phone_number, generate_profile

HUMAN_FIRST = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Isaac", "Julia"]
HUMAN_LAST= ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Clark", "Lewis", "Walker", "Young", "Hall"]
FANTASY_NAMES = ["Zorblax", "Elandra", "Thrain", "Myrrha", "Drakar", "Lyssara", "Volgrim", "Zenthra", "Kaelith", "Orvax"]

# Test generate_name function with human type
# Test if the generate name function is good with its iteration of generating list of human names (last + first name)
def test_generate_name_human_multiple():
    result = generate_name(type="human", length=3)
    assert isinstance(result, list)
    assert len(result) == 3  
    assert all(isinstance(name, str) and " " in name for name in result)  # All should be valid names

    # Ensure the expected format with valid first and last for all the names generated
    for name in result:
        first, last = name.split(" ")
        assert first in HUMAN_FIRST
        assert last in HUMAN_LAST

# Test if the generate name function can properly generate one human name
def test_generate_name_human_single():
    result = generate_name(type="human", length=1)
    assert isinstance(result, list)
    assert len(result) == 1  
    assert " " in result[0]  # Ensure first and last name exist

    # Ensure the expected format with valid first and last
    first, last = result[0].split(" ")
    assert first in HUMAN_FIRST
    assert last in HUMAN_LAST

# Test generate_name function with fantasy type
# Test if the generate name function is good with its iteration of generating list of fantasy names
def test_generate_name_fantasy_multiple():
    result = generate_name(type="fantasy", length=3)
    assert isinstance(result, list)
    assert len(result) == 3 
    assert all(isinstance(name, str) and " " not in name for name in result)  # Fantasy names should contain no space
    # Ensure each name is valid fantasy names
    for name in result:
        assert name in FANTASY_NAMES

# Test if the generate name function can properly generate one fantasy name
def test_generate_name_fantasy_single():
    result = generate_name(type="fantasy", length=1)
    assert isinstance(result, list)
    assert len(result) == 1  
    assert " " not in result[0]  # Ensure no space
    # Ensure valid fantasy name
    assert result[0] in FANTASY_NAMES

# Test if the generate name function can handle empty cases
def test_generate_name_human_zero():
    result = generate_name(type="human", length=0)
    assert isinstance(result, list)
    assert len(result) == 0  # Should return an empty list

    result = generate_name(type="fantasy", length=0)
    assert isinstance(result, list)
    assert len(result) == 0  # Should return an empty list

# Test function does not silently return empty names
def test_generate_name_not_empty():
    result = generate_name(type="human", length=2)
    assert all(name.strip() != "" for name in result)  

    result = generate_name(type="fantasy", length=2)
    assert all(name.strip() != "" for name in result)

# Edge case: Invalid type input, we want the user to choose from human or fantasy
# Representative invalid types
@pytest.mark.parametrize("invalid_type", ["alien", "humen", "fantacy", "unknown", "HUMAN", "FANTASY", 123, True, False, None])
def test_generate_name_invalid_type(invalid_type):
    with pytest.raises(ValueError):
        generate_name(type=invalid_type, length=2) 


STREETS = ["123 Maple St", "456 Oak Ave", "789 Pine Rd", "101 Elm St", "202 Birch Blvd", "303 Cedar Ln", "404 Spruce Ct", "505 Walnut Way"]
CITIES = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
US_POSTCODES = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101"]
UK_POSTCODES = ["EC1A 1BB", "W1A 0AX", "M1 1AE", "B33 8TH", "CR2 6XH", "DN55 1PT", "E1 6AN", "N1 9GU"]

# Test if the generate address function generate correct address for country US
# Test the correctness of generating short address
def test_generate_address_us_short():
    result = generate_address(country = "US", format = "short")
    assert isinstance(result, str)
    
    # Check individual components
    parts = result.split(", ")
    assert len(parts) == 2 
    street, city = parts
    # must have one valid street, one valid city
    assert street in STREETS
    assert city in CITIES
    assert not any(postcode in result for postcode in US_POSTCODES) # no postal code in short
    assert "USA" not in result # no country in short

# Test the correctness of generating long address
def test_generate_address_us_long():
    result = generate_address(country = "US", format = "long")
    assert isinstance(result, str)

    # Check individual components
    parts = result.split(", ")
    assert len(parts) == 4
    street, city, postcode, country = parts
    # must have one valid street, city, postcode, country
    assert street in STREETS
    assert city in CITIES
    assert any(postcode in result for postcode in US_POSTCODES) # contains valid us postal code
    assert "USA" in result

# Test if the generate address function generate correct address for country uk
# Test the correctness of generating short address
def test_generate_address_uk_short():
    result = generate_address(country = "UK", format = "short")
    assert isinstance(result, str)

    # Check individual components
    parts = result.split(", ")
    assert len(parts) == 2
    street, city = parts
    # must have one valid street, city
    assert street in STREETS
    assert city in CITIES
    assert not any(postcode in result for postcode in UK_POSTCODES) # no postal code in short
    assert "UK" not in result # no country in short

# Test the correctness of generating long address
def test_generate_address_uk_long():
    result = generate_address(country = "UK", format = "long")
    assert isinstance(result, str)

    # Check individual components
    parts = result.split(", ")
    assert len(parts) == 4
    street, city, uk_postcode, country = parts
    # must have one valid street, city, postcode, country
    assert street in STREETS
    assert city in CITIES
    assert any(postcode in result for postcode in UK_POSTCODES) # contains valid us postal code
    assert "UK" in result

# Test empty country input
def test_generate_address_empty_country():
    with pytest.raises(ValueError):
        generate_address(country="", format="short")

# Test empty format input
def test_generate_address_empty_format():
    with pytest.raises(ValueError):
        generate_address(country="US", format="")

# Test function does not silently return empty string
def test_generate_address_not_empty():
    result = generate_address(country="US", format="short")
    assert result.strip() != ""

# Edge case: Test invalid country inputs
# Representative invalid countries
@pytest.mark.parametrize("invalid_country", ["France", "Germany", "Us", "us", "uS", "Uk", "uk", "uK", 123, True, False, None])
def test_generate_address_invalid_country(invalid_country):
    with pytest.raises(ValueError):
        generate_address(country=invalid_country, format="short")

# Edge case: Test invalid format inputs
# Representative invalid format
@pytest.mark.parametrize("invalid_format", ["SHORT", "LONG", "medium", 123, True, False, None])
def test_generate_address_invalid_country(invalid_format):
    with pytest.raises(ValueError):
        generate_address(country="US", format=invalid_format)

