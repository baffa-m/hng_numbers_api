from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .math_func import get_properties, get_digit_sum, get_fun_fact, is_prime, is_perfect
# Create your views here.

@api_view(['GET'])
def num_properties(request):
    try:
        number = int(request.GET.get('number', ''))
    except ValueError:
        return Response(
            {"number": request.GET.get('number', ''), "error": True},
            status=status.HTTP_400_BAD_REQUEST
        )

    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": get_properties(number),
        "digit_sum": get_digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    
    return Response(response_data)