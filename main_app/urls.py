from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('breeds/', views.BreedList.as_view(), name="breed_list"),
    path('breeds/new', views.BreedCreate.as_view(), name="breed_create"),
    path('breeds/<int:pk>/', views.BreedDetail.as_view(), name="breed_detail"),
    path('breeds/<int:pk>/update', views.BreedUpdate.as_view(), name="breed_update"),
    path('breeds/<int:pk>/detele', views.BreedDelete.as_view(), name="breed_delete"),
    path('breeds/<int:pk>/breeders/new', views.BreederCreate.as_view(), name="breeder_create"),
]

