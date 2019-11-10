from django.db import models


# Create your models here.

class Country(models.Model):
    class Meta:
        verbose_name_plural = "Countries"

    name = models.TextField()

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' (' + self.country.name + ')'


class Art(models.Model):
    CHOICES = (
        ('p', 'Painting'),
        ('m', 'Music'),
        ('f', 'Film'),
        ('d', 'Digital')
    )

    title = models.TextField()
    date = models.DateField()
    type = models.CharField(max_length=1, choices=CHOICES)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by ' + self.artist.name + ' (' + self.date.year.__str__() + ')'
