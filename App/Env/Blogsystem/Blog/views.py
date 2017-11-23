from django.shortcuts import render

# Create your views here.
def index(request):

    context ={"title":"Home Page content"}
    return render(request, "Blog/index.html",context)