# Pypal - A Random Profile Generator

Pypal is a Python package that generates profiles with random human-like and fantasy names, US or UK addresses, domestic or international phone numbers, and emails. It is useful for testing, development, and anonymized data generation.
![Build Status](https://github.com/software-students-spring2025/3-python-package-pypal/actions/workflows/event-logger.yml/badge.svg)

## Installation

If you want to import the package, install from: [PyPI](A LINK TO PACKAGE PAGE ON PYPI) using pip:

```sh 
pip install nyu-pypal
```

## Usage
### **Function: generate_name**
Generates a random name (either a **human name** or a **fantasy name**).

#### **Parameters**
- `type` (*str*): `"human"` or `"fantasy"`, determining the type of name generated.
- `length` (*int*): The number of names to generate.

#### **Returns**
- `list[str]`: A list of generated names.

#### **Example**
```python
from pypal.generator import generate_name

# Generate a single human name
print(generate_name(type="human", length=1))

# Generate multiple fantasy names
print(generate_name(type="fantasy", length=3))
```
#### **Link to Python Program**


### **Function: generate_address**
Generates a random address in **US or UK format**, either in a **short** or **long** version.

#### **Parameters**
- **`country`** (*str*):  
  - `"US"` → Generates a US-based address.  
  - `"UK"` → Generates a UK-based address.  
- **`format`** (*str*):  
  - `"short"` → Returns `street, city`.  
  - `"long"` → Returns `street, city, postal_code, country`.

#### **Returns**
- `str`: A properly formatted address.

#### **Example**
```python
from pypal.generator import generate_address

# Generate a US address in short format
print(generate_address(country="US", format="short"))

# Generate a UK address in long format
print(generate_address(country="UK", format="long"))
```
#### **Link to Python Program**


### **Function: `generate_phone_number`**
Generates a **random US phone number**, either in **domestic format** or with an **international country code**.

#### **Parameters**
- **`style`** (*str*):  
  - `"domestic"` → Generates a US phone number like `(XXX) XXX-XXXX`.  
  - `"international"` → Generates a phone number with country code `+1-XXX-XXX-XXXX`.

#### **Returns**
- `str`: A properly formatted phone number.

#### **Example Usage**
```python
from pypal.generator import generate_phone_number

# Generate a domestic phone number
print(generate_phone_number(style="domestic"))

# Generate an international phone number
print(generate_phone_number(style="international"))
```
#### **Link to Python Program**


### **Function: `generate_profile`**
Generates a **full random user profile**, including a **name, address, phone number, and email**.

#### **Parameters**
- **`include_email`** (*bool*, default=`True`):  
  - `True` → Includes a generated email.  
  - `False` → Excludes the email field.  
- **`include_phone`** (*bool*, default=`True`):  
  - `True` → Includes a generated phone number.  
  - `False` → Excludes the phone field.  

#### **Returns**
- `dict`: A dictionary containing:
  - **`"name"`** (*str*): A randomly generated full name.  
  - **`"address"`** (*str*): A randomly generated address.  
  - **`"email"`** (*str*, optional): A generated email (`first@example.com`).  
  - **`"phone"`** (*str*, optional): A generated phone number.  

#### **Example Usage**
```python
from pypal.generator import generate_profile

# Generate a full profile with email & phone
print(generate_profile(include_email=True, include_phone=True))

# Generate a profile with only a name & address
print(generate_profile(include_email=False, include_phone=False))
```
#### **Link to Python Program**


## Contributing

We welcome contributions from the community! Follow these steps to set up your development environment:

### **1. Clone the Repository**
Fork the repository on GitHub, then clone your fork locally:
```sh
git clone https://github.com/software-students-spring2025/3-python-package-pypal.git
cd 3-python-package-pypal
```

### **2. Set Up Virtual Environment**
Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### **3. Install Dependencies**
Install all required packages:
```sh
pip install -r requirements.txt
```

### **4. Build the Package**
Build the pacakge locally:
```sh
pip install .
```

### **5. Run Unit Tests**
Ensure all tests pass before submitting a pull request:
```sh
cd tests
pytest test_generator.py
```

### **6. Make Your Contributions**
#### **1. Create a new branch:**
```sh
git checkout -b your-feature-branch
```
#### **2. Make your changes and commit:**
```sh
git add .
git commit -m "Describe your changes"
```
#### **3. Push to your fork:**
```sh
git push origin your-feature-branch
```
#### **4. Create pull request from your fork to the main repository.**

## Teammates
[Sophia Gu](https://github.com/Sophbx)
[Jason Lin](https://github.com/JasonLIN0226)
[Allen Ni](https://github.com/AllenNi66)
[Zifan Zhao](https://github.com/Exiam6)

## Running the Project on Any Platform


## Environment Variables & Data Setup