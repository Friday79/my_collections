from django.shortcuts import render

# Create your views here.
def index(request):
    """ created views to return the index page """

    return render(request, 'home/index.htnl')