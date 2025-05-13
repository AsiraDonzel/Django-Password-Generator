import random
import string
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'generator/index.html')

def generate_password(request):
    length = int(request.GET.get('length', 12))  # Default 12 characters
    use_upper = request.GET.get('uppercase', 'false') == 'true'
    use_numbers = request.GET.get('numbers', 'false') == 'true'
    use_symbols = request.GET.get('symbols', 'false') == 'true'

    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return JsonResponse({'password': password})
