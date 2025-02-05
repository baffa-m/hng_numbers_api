# Number Properties API

A Django REST Framework API that analyzes numbers and returns their mathematical properties along with interesting facts.

## Description

This API takes a number as input and returns various mathematical properties including:
- Prime number status
- Perfect number status
- Armstrong number checking
- Odd/Even classification
- Digit sum calculation
- Mathematical fun fact from Numbers API

## Technologies Used

- Python 3.8+
- Django 5.0+
- Django REST Framework
- django-cors-headers
- Requests (for Numbers API integration)

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Local Development

1. Clone the repository
```bash
git clone https://github.com/baffa-m/hng_numbers_api
cd hng_numbers_api
```

2. Create and activate a virtual environment
```bash
python -m venv env
source env\bin\activate 
```

3. Install dependencies
```bash
pip install -r requirements.txt
```


4. Run the development server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## API Documentation

### Endpoint

- URL: `GET /api/classify-number`
- Query Parameter: `number` (integer)
- Description: Returns mathematical properties and fun fact about the provided number

### Response Format

#### Success Response (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request):
```json
{
    "number": "invalid_input",
    "error": true
}
```

### Example Usage

Using curl:
```bash
curl "https://baffam.pythonanywhere.com/api/classify-number?number=371"
```


## Mathematical Properties

The API checks for several mathematical properties:

1. Prime Numbers: Numbers greater than 1 that have no positive divisors other than 1 and themselves.
2. Perfect Numbers: Numbers that are equal to the sum of their proper divisors.
3. Armstrong Numbers: Numbers that are equal to the sum of their own digits raised to the power of the number of digits.
4. Properties Array combinations:
   - ["armstrong", "odd"] - Armstrong numbers that are odd
   - ["armstrong", "even"] - Armstrong numbers that are even
   - ["odd"] - Odd numbers that aren't Armstrong numbers
   - ["even"] - Even numbers that aren't Armstrong numbers


## Deployment

The API can be deployed to:
- PythonAnywhere
- Heroku


