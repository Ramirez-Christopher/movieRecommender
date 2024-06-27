from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from django.http import HttpResponse
from .services import get_popular_movies
import os

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the minder index.")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    template_name = 'signup.html'

def popular_movies(request):
    api_key = os.getenv('API_KEY')
    movies_data = get_popular_movies(api_key)
    if movies_data:
        return JsonResponse(movies_data)  # movies_data is already a dictionary
    else:
        return JsonResponse({'error': 'Failed to fetch popular movies'}, status=500)