from django.urls import path

from django.conf.urls.static import static
from django.conf import settings


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    #Create new listing path
    path("create", views.create_listing, name="create"),
    #Active Listings path
    path("listing/<int:listing_id>", views.show_listing, name="listing"),
    #Watchlist path
    path("watchlist", views.watchlist, name="watchlist"),
    #Categories path
    path("categories", views.categories, name="categories"),
    path("categories/<str:category>", views.show_category_listings, name="show"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
