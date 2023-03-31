from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=60)
    releaseDate = models.DateField()
    rating = models.FloatField()

    class Meta:
        db_table = 'movie'