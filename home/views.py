from django.shortcuts import render

# Create your views here.
def index(request):
    *** creating views for index ***
    
    return render(request, 'home/index.htnl')