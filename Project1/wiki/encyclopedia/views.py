from django import forms
from django.shortcuts import render
from markdown2 import Markdown

markdowner = Markdown()

class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass', 'placeholder': 'Search'}))


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entries = util.list_entries()
    if title in entries:
        page = util.get_entry(title)
        page_converted = markdowner.convert(page)

        context = {
            'page': page_converted,
            'title': title,
            'form': Search()
        }
        return render(request, "encyclopedia/entry.html", context)

    else:
        return render(request, "encyclopedia/error.html", {"message": "The requested page was not found.", "form":Search()})

