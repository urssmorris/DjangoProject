from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def CSS(request):
    return render(request, "encyclopedia/CSS.html", {
        "entries": util.list_entries()
    })
