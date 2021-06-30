from django.contrib.auth.models import AbstractUser
from django.db import models


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

#Bids
class Bid(models.Model):
    time = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user} put a bid in for {self.price}"

#Comment
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_coms")
    title = models.CharField(max_length=25, default="")
    comment = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, blank=True)

#Create listing model
class Listing(models.Model):
    item = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default= "0.00")
    category = models.CharField(max_length=1, choices=CATEGORIES, default=CATEGORIES[5][1])
    time = models.DateTimeField(auto_now_add=True, blank=True)
    closed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owners")
    bids = models.ManyToManyField(Bid, blank=True, related_name="bids")
    comments = models.ManyToManyField(Comment, blank=True, related_name="comments")
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.item}: is {self.price} and is being sold by {self.owner}"

