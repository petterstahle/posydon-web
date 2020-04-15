from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#These are function based views. Class defined views are also available with the django framework (more generic but also complicated)


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user) #print the user requesting the home page in the console
    return render(request, "home.html", {}) #string of HTML

def about_view(request, *args, **kwargs):
    print(request)
    context = {
        "title": "This is info about the project.",
        "current_description": "",
        "current_objective": "",
    }
    return render(request, "about.html", context)
