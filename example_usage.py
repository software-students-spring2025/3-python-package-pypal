import random
from pypal import generate_profile, generate_date_of_birth

def generate_extended_profile(include_email=True, include_phone=True, include_dob=True, include_occupation=True, include_bio=True):
    """
    Generates an extended profile including additional details with our pypal package:
      - Date of Birth (dob)
      - Occupation
      - A short bio

    """
    profile = generate_profile(include_email, include_phone)

    if include_dob:
        profile["dob"] = generate_date_of_birth()

    if include_occupation:
        occupations = [
            "Software Engineer", "Doctor", "Teacher", "Artist", "Musician",
            "Writer", "Scientist", "Architect", "Chef", "Designer"
        ]
        profile["occupation"] = random.choice(occupations)

    if include_bio:
        bios = [
            "Loves exploring new technologies and creative problem solving.",
            "Avid reader and coffee enthusiast.",
            "Passionate about art, music, and design.",
            "Enjoys traveling and experiencing new cultures.",
            "Dedicated to continuous learning and innovation."
        ]
        profile["bio"] = random.choice(bios)

    return profile

if __name__ == "__main__":
    extended_profile = generate_extended_profile()
    print("Extended Profile:")
    for key, value in extended_profile.items():
        print(f"{key}: {value}")