from django.contrib.auth.models import AbstractUser
from django.db import models

#Listing categories
CATEGORIES = (
    ('a', 'Microprocessors'),
    ('b', 'Motherboards'),
    ('c', 'Computer Memory (RAM)'),
    ('d', 'Hard Disk Drives'),
    ('e', 'Computer Case'),
    ('f', 'Monitors'),
    ('g', 'Periferics'),
    ('h', 'Others')
)

class User(AbstractUser):
    pass
    #customer_id = models.CharField(max_length=100, blank=True, null=True)

#Bid model
class Bid(models.Model):
    time = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    price = models.DecimalField('Bid', max_digits=10, decimal_places=2, default= "0.00")

    def __str__(self):
        return f"{self.user} put a bid in for {self.price}"

#Comment model
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_coms")
    title = models.CharField(max_length=25, default="")
    comment = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now_add=True, blank=True)

#Create auction listing model
class Listing(models.Model):
    item = models.CharField('Title', max_length=64)
    price = models.DecimalField('Starting Bid', max_digits=10, decimal_places=2, default= "0.00")
    description = models.TextField(max_length=300, blank=True)
    category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[0][0])
    time = models.DateTimeField(auto_now_add=True, blank=True)
    closed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owners")
    bids = models.ManyToManyField(Bid, blank=True, related_name="bids")
    comments = models.ManyToManyField(Comment, blank=True, related_name="comments")
    image = models.ImageField(upload_to='auction/images/', default='auctions/images/default.jpg')
    

    def __str__(self):
        return f"{self.item}: is {self.price} and is being sold by {self.owner}"

#Wacthlist model
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")
    watched = models.ManyToManyField(User, related_name="watchlist_btn")
    
    def __str__(self):
        return f"{self.user.username} listed {self.listing.id}"