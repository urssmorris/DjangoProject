from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

#Import login_required library
from django.contrib.auth.decorators import login_required
#Import models
from .models import *
#Import forms
from .forms import *


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

#Create Listing view
@login_required
def create_listing(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user)
        form = ListingForm(request.POST, request.FILES)
        #Check form and save listing 
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = user
            listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create.html", {
                #Return ListingForm as form
                "form": form
            })
    else:
        return render(request, "auctions/create.html", {
            "form": ListingForm()
        })

#Watchlist view
@login_required
def watchlist(request):
    user = User.objects.get(username=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlist": user.watchlist.all()
    })

#Show active listing
@login_required
def show_listing(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    user = User.objects.get(username=request.user)
    if request.method == "POST":

        # Add/Remove from Watchlist 
        if request.POST.get("button") == "Watchlist":
            watched = False
            if not user.watchlist.filter(listing = listing):
                watchlist = Watchlist()
                watchlist.user = user
                watchlist.listing = listing
                watchlist.save()
                watched = True  
            else:
                user.watchlist.filter(listing=listing).delete()
                watched = False
            return render(request, 'auctions/listing.html', {
                "listing": listing,
                "watched": watched,
                "form": BidForm()
                })

            
        if not listing.closed:
            if request.POST.get("button") == "Close": 
                listing.closed = True
                listing.save()
            else:
                price = float(request.POST["price"])
                # bids = listing.bids.all()
                # only let those who dont own the listing be able to bid
                if user.username != listing.owner.username: 
                    if price <= listing.price:
                        return render(request, "auctions/listing.html", {
                            "listing": listing,
                            "form": BidForm(),
                            "message": "Invalid Bid Amount!"
                        })
                    form = BidForm(request.POST)
                    if form.is_valid():
                        bid = form.save(commit=False)
                        bid.user = user
                        bid.save()
                        listing.bids.add(bid)
                        listing.price = price
                        listing.save()
                    else:
                        return render(request, 'auctions/listing.html', {
                            "form": form
                        })
        return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
    else:
        # Category name from index
        category = listing.category
        cat = dict(CATEGORIES)
        watched = False
        if user.watchlist.filter(listing=listing):
            watched = True
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "form": BidForm(),
            "category": cat[category],
            "watched": watched
        })


def comment(request, listing_id):
    user = User.objects.get(username=request.user)
    listing = Listing.objects.get(pk=listing_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = user
            comment.save()
            listing.comments.add(comment)
            listing.save()

            return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
        else:
            return render(request, "auctions/comment.html", {
                "form": form,
                "listing_id": listing.id,
            })
    else:
        return render(request, "auctions/comment.html", {
            "form": CommentForm(),
            "listing_id": listing.id            
        })

@login_required
def categories(request):
    return render(request, 'auctions/categories.html', {
        "categories": CATEGORIES,
    })

@login_required
def show_category_listings(request, category):
    listings = Listing.objects.filter(category__in = category[0])
    cat = dict(CATEGORIES)
    return render(request, 'auctions/category.html', {
        "listings": listings,
        "category": cat[category]
    })