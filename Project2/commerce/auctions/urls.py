from django.urls import path

from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #Create listing path
    path("create", views.create_listing, name="create"),
]
