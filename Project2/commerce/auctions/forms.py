from typing import AbstractSet
from django.forms import ModelForm
from .models import *

#Listing form
class ListingForm(ModelForm):
  class Meta:
    model = Listing
    fields = ['item', 'price', 'description', 'category', 'image']

#Bud form
class BidForm(ModelForm):
  class Meta:
    model = Bid
    fields = ["price"]

#Comment form
class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ["title", "comment"]