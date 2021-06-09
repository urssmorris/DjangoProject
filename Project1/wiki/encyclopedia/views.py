from django.shortcuts import redirect, render
from . import util
from markdown2 import markdown
from random import randint


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#Entry function (Markdown to HTML Conversion)
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
    
#Create page function
def create(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        pretitle = "#"+title+"\n"
        content = request.POST.get("content").strip()
        if title == "" or content == "":
            return render(request, "encyclopedia/create.html", {"message": "Both fields must be filled", "title": title, "content": content})
        if title in util.list_entries():
            return render(request, "encyclopedia/create.html", {"message": "Title already exist", "title": title, "content": content})
        util.save_entry(title, pretitle + content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/create.html")

#Edit function
def edit(request, title):
    content = util.get_entry(title.strip())
    if content == None:
        return render(request, "encyclopedia/edit.html", {'error': "404 Not Found"})

    if request.method == "POST":
        content = request.POST.get("content").strip()
        if content == "":
            return render(request, "encyclopedia/edit.html", {"message": "Can't save with empty field.", "title": title, "content": content})
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {'content': content, 'title': title})

# Random page function
def randomPage(request):
    entries = util.list_entries()
    randomTitle = entries[randint(0, len(entries)-1)]
    return redirect("entry", title=randomTitle)