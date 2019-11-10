from django.urls import path

from weiland.backend import views

urlpatterns = [
    path('country/', views.country_list),
    path('country/<int:id>/', views.country_update_delete),
    path('artist/', views.artist_list),
    path('artist/<int:id>/', views.artist_update_delete),
    path('art/', views.art_list),
    path('art/<int:id>/', views.art_update_delete)
]
