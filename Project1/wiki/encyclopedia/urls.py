from django.urls import path

from . import views

urlpatterns = [
    path("wiki", views.index, name="index"),
    #Entry path
    path("wiki/<title>", views.entry, name="entry"),
    #Search path
    path("search", views.search, name="search")
]
