from typing import AbstractSet
from django.forms import ModelForm
from .models import *


class ListingForm(ModelForm):
  class Meta:
    model = Listing
    fields = ['item', 'price', 'description', 'category', 'image']

   