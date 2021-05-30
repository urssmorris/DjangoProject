from django.shortcuts import redirect, render
from . import util
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#Entry function
def entry(request, title):
    content = util.get_entry(title.strip())
    if content == None:
        content = "# Page not found"
    content = markdown(content)
    return render(request, "encyclopedia/entry.html", {'content': content, 'title': title})

#Search function
def search(request):
    q = request.GET.get('q').strip()
    if q in util.list_entries():
        return redirect("entry", title = q)
    return render(request, "encyclopedia/search.html", {"entries": util.search(q), "q":q})
    
