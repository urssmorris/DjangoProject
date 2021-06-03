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
    
#Create page function
def create(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = "#"+title +"\n"+ request.POST.get("content").strip()
        if title == "" or content == "":
            return render(request, "encyclopedia/create.html", {"message": "Can't save with empty field.", "title": title, "content": content})
        if title in util.list_entries():
            return render(request, "encyclopedia/create.html", {"message": "Title already exist. Try another.", "title": title, "content": content})
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/create.html")