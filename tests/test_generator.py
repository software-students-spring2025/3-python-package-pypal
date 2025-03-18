import pytest
from pypal.generator import generate_name, generate_address, generate_phone_number, generate_profile


# Test generate_name function with human type
# Test if the generate name function is good with its iteration of generating list of human names (last + first name)
def test_generate_name_human_multiple():
    result = generate_name(type="human", length=3)
    assert isinstance(result, list)
    assert len(result) == 3  
    assert all(isinstance(name, str) and " " in name for name in result)  # All should be valid names


# Test if the generate name function can properly generate one human name
def test_generate_name_human_single():
    result = generate_name(type="human", length=1)
    assert isinstance(result, list)
    assert len(result) == 1  
    assert " " in result[0]  # Ensure first and last name exist


# Test generate_name function with fantasy type
# Test if the generate name function is good with its iteration of generating list of fantasy names
def test_generate_name_fantasy_multiple():
    result = generate_name(type="fantasy", length=3)
    assert isinstance(result, list)
    assert len(result) == 3 
    assert all(isinstance(name, str) and " " not in name for name in result)  # Fantasy names should NOT contain spaces


# Test if the generate name function can properly generate one fantasy name
def test_generate_name_fantasy_single():
    result = generate_name(type="fantasy", length=1)
    assert isinstance(result, list)
    assert len(result) == 1  
    assert " " not in result[0]  # Ensure it does NOT contain a space 


# Test if the generate name function can handle empty cases
def test_generate_name_human_zero():
    result = generate_name(type="human", length=0)
    assert isinstance(result, list)
    assert len(result) == 0  # Should return an empty list

    result = generate_name(type="fantasy", length=0)
    assert isinstance(result, list)
    assert len(result) == 0  # Should return an empty list


# Edge case: Invalid type input, we want the user to choose from human or fantasy
# Representative invalid types
@pytest.mark.parametrize("invalid_type", ["alien", "humen", "fantacy", "unknown", 123, True, False, None])
def test_generate_name_invalid_type(invalid_type):
    with pytest.raises(ValueError):
        generate_name(type=invalid_type, length=2) 
