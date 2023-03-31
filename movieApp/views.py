from django.shortcuts import render
from .models import Movie


# Create your views here.
def movieList(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies':movies})
