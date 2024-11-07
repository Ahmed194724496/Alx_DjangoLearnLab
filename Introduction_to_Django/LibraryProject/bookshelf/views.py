from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Add docstring and improve the response
    """View function for the home page of the site."""
    return HttpResponse("<h1>Welcome to my library!</h1>")