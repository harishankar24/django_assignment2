from django.shortcuts import render
from .models import Movie
from .forms import MovieForm


# Create your views here.
def movieList(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies':movies})


def addMovie(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return movieList(request)
    return render(request, 'addMovie.html', {'form':form})