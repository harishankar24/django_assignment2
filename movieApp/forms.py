from django.forms import ModelForm, DateInput
from .models import Movie


class DateInput(DateInput):
    input_type = 'date'


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'releaseDate', 'rating']
        widgets = {
            'releaseDate': DateInput,
        }