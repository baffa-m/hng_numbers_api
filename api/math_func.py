import math
import requests
from typing import List

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    n = abs(n)
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    n = abs(n)
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def get_digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

def get_properties(n: int) -> List[str]:
    return (["armstrong", "even" if n % 2 == 0 else "odd"] if is_armstrong(n) else (["even"] if n % 2 == 0 else ["odd"]))

def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
        return f"{n} is a number with interesting mathematical properties."
    except:
        return f"{n} is a number with interesting mathematical properties."