from django.contrib import admin

from . import models


# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = (['name'])
    list_filter = (['name'])
    search_fields = (['name'])
    sortable_by = (['name'])


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = (['country'])
    search_fields = (['name'])
    sortable_by = (['name'])


class ArtAdmin(admin.ModelAdmin):
    list_display = (['title', 'date', 'type', 'description', 'artist'])
    list_filter = (['artist'])
    search_fields = (['title'])
    sortable_by = (['date'])


admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.Artist, ArtistAdmin)
admin.site.register(models.Art, ArtAdmin)
