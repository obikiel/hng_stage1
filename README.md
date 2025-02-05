# Number Classification API

This is a Django-based API that classifies numbers and returns interesting mathematical properties along with a fun fact.

## Endpoint

- **GET** `/api/classify-number?number=<number>`

## Response Format

### 200 OK
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}