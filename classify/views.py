import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def classify_number(request):
    number = request.GET.get('number', None)
    
    if number is None or not number.lstrip('-').isdigit():
        return JsonResponse({"number": number, "error": True}, status=400)
    
    number = int(number)
    
    # Check if the number is prime
    is_prime = is_prime_number(number)
    
    # Check if the number is perfect
    is_perfect = is_perfect_number(number)
    
    # Get properties of the number
    properties = get_number_properties(number)
    
    # Calculate the sum of its digits
    digit_sum = sum(int(digit) for digit in str(abs(number)))
    
    # Get a fun fact from the Numbers API
    fun_fact = get_fun_fact(number)
    
    response = {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }
    
    return JsonResponse(response, status=200)

def is_prime_number(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_number(n):
    if n <= 1:
        return False
    sum_divisors = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
        i += 1
    return sum_divisors == n

def get_number_properties(n):
    properties = []
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    if is_armstrong_number(n):
        properties.append("armstrong")
    return properties

def is_armstrong_number(n):
    n_abs = abs(n)  # Use absolute value to ignore the negative sign
    digits = [int(d) for d in str(n_abs)]  # Convert digits to integers
    num_digits = len(digits)
    return n_abs == sum(d ** num_digits for d in digits) 

def get_fun_fact(n):
    url = f"http://numbersapi.com/{n}/math"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        return f"No fun fact available due to an error: {e}"